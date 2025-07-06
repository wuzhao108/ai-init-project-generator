# -*- coding: utf-8 -*-
"""
模板管理器模块
负责模板的创建、读取、操作和删除
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

from ..utils.file_utils import ensure_dir, file_exists, read_file, write_file


class TemplateManager:
    """模板管理器"""
    
    def __init__(self, templates_dir: str = None):
        """
        初始化模板管理器
        
        Args:
            templates_dir: 模板目录路径，默认为项目根目录下的templates目录
        """
        if templates_dir is None:
            # 获取项目根目录
            project_root = Path(__file__).parent.parent.parent
            templates_dir = project_root / "templates"
        
        self.templates_dir = Path(templates_dir)
        
        # 确保模板目录存在
        ensure_dir(str(self.templates_dir))
    
    def list_templates(self) -> List[str]:
        """
        列出所有可用的模板文件
        
        Returns:
            List[str]: 模板文件名称列表（不包含.md扩展名）
        """
        template_files = []
        if self.templates_dir.exists():
            for file_path in self.templates_dir.glob("*.md"):
                template_files.append(file_path.stem)
        return sorted(template_files)
    
    def template_exists(self, template_name: str) -> bool:
        """
        检查模板文件是否存在
        
        Args:
            template_name: 模板文件名称（不包含.md扩展名）
            
        Returns:
            bool: 模板文件是否存在
        """
        template_name = self._sanitize_filename(template_name)
        template_file = self.templates_dir / f"{template_name}.md"
        return file_exists(str(template_file))
    
    def load_template(self, template_name: str) -> str:
        """
        加载模板文件内容
        
        Args:
            template_name: 模板文件名称（不包含.md扩展名）
            
        Returns:
            str: 模板文件内容
            
        Raises:
            FileNotFoundError: 模板文件不存在
        """
        template_name = self._sanitize_filename(template_name)
        template_file = self.templates_dir / f"{template_name}.md"
        
        if not file_exists(str(template_file)):
            raise FileNotFoundError(f"模板文件不存在：{template_file}")
        
        return read_file(str(template_file))
    
    def save_template(self, content: str, template_name: str = None) -> str:
        """
        保存模板内容到文件
        
        Args:
            content: 模板内容
            template_name: 模板文件名称，如果不提供则使用默认名称
            
        Returns:
            str: 模板文件路径
            
        Raises:
            ValueError: 模板内容无效
            IOError: 文件写入失败
        """
        # 验证模板内容
        if not content or not content.strip():
            raise ValueError("模板内容不能为空")
        
        # 确定模板文件名
        if template_name is None:
            template_name = f"template_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        template_name = self._sanitize_filename(template_name)
        template_file = self.templates_dir / f"{template_name}.md"
        
        try:
            write_file(str(template_file), content)
            return str(template_file)
        except Exception as e:
            raise IOError(f"保存模板文件失败：{str(e)}")
    
    def delete_template(self, template_name: str) -> bool:
        """
        删除模板文件
        
        Args:
            template_name: 模板文件名称（不包含.md扩展名）
            
        Returns:
            bool: 是否删除成功
        """
        template_name = self._sanitize_filename(template_name)
        template_file = self.templates_dir / f"{template_name}.md"
        
        if file_exists(str(template_file)):
            try:
                os.remove(str(template_file))
                return True
            except Exception:
                return False
        return False
    
    def get_template_path(self, template_name: str) -> str:
        """
        获取模板文件的完整路径
        
        Args:
            template_name: 模板文件名称（不包含.md扩展名）
            
        Returns:
            str: 模板文件完整路径
        """
        template_name = self._sanitize_filename(template_name)
        template_file = self.templates_dir / f"{template_name}.md"
        return str(template_file)
    
    def extract_templates_from_markdown(self, content: str) -> Dict[str, str]:
        """
        从Markdown内容中提取模板
        
        Args:
            content: Markdown文件内容
            
        Returns:
            Dict[str, str]: 模板名称到模板内容的映射
        """
        templates = {}
        
        # 使用正则表达式提取模板块
        # 匹配格式: ### template_name.j2\n```jinja2\n...\n```
        pattern = r'### ([^\n]+\.j2)\s*\n```jinja2\n(.*?)\n```'
        matches = re.findall(pattern, content, re.DOTALL)
        
        for template_name, template_content in matches:
            templates[template_name] = template_content.strip()
        
        return templates
    
    def get_template_info(self, template_name: str) -> Dict[str, Any]:
        """
        获取模板文件信息
        
        Args:
            template_name: 模板文件名称
            
        Returns:
            Dict[str, Any]: 模板文件信息
        """
        template_file = self.get_template_path(template_name)
        
        if not file_exists(template_file):
            return {}
        
        try:
            content = self.load_template(template_name)
            stat = os.stat(template_file)
            
            # 提取模板信息
            templates = self.extract_templates_from_markdown(content)
            
            return {
                "name": template_name,
                "path": template_file,
                "template_count": len(templates),
                "template_names": list(templates.keys()),
                "file_size": stat.st_size,
                "modified_time": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "content_preview": content[:200] + "..." if len(content) > 200 else content
            }
        except Exception:
            return {
                "name": template_name,
                "path": template_file,
                "error": "Failed to load template"
            }
    
    def copy_template(self, source_template: str, target_template: str) -> str:
        """
        复制模板文件
        
        Args:
            source_template: 源模板名称
            target_template: 目标模板名称
            
        Returns:
            str: 目标模板文件路径
            
        Raises:
            FileNotFoundError: 源模板文件不存在
            IOError: 复制失败
        """
        if not self.template_exists(source_template):
            raise FileNotFoundError(f"源模板文件不存在：{source_template}")
        
        try:
            content = self.load_template(source_template)
            return self.save_template(content, target_template)
        except Exception as e:
            raise IOError(f"复制模板文件失败：{str(e)}")
    
    def export_template(self, template_name: str, export_path: str) -> None:
        """
        导出模板文件到指定路径
        
        Args:
            template_name: 模板文件名称
            export_path: 导出路径
            
        Raises:
            FileNotFoundError: 模板文件不存在
            IOError: 导出失败
        """
        content = self.load_template(template_name)
        
        try:
            write_file(export_path, content)
        except Exception as e:
            raise IOError(f"导出模板文件失败：{str(e)}")
    
    def import_template(self, import_path: str, template_name: str = None) -> str:
        """
        从指定路径导入模板文件
        
        Args:
            import_path: 导入路径
            template_name: 模板文件名称，如果不提供则从文件名获取
            
        Returns:
            str: 保存的模板文件路径
            
        Raises:
            FileNotFoundError: 导入文件不存在
            ValueError: 模板文件格式无效
        """
        if not file_exists(import_path):
            raise FileNotFoundError(f"导入文件不存在：{import_path}")
        
        try:
            content = read_file(import_path)
            
            if template_name is None:
                # 从文件路径提取文件名
                template_name = Path(import_path).stem
            
            return self.save_template(content, template_name)
        except Exception as e:
            raise ValueError(f"导入模板文件失败：{str(e)}")
    
    def _sanitize_filename(self, filename: str) -> str:
        """
        清理文件名，移除不安全字符
        
        Args:
            filename: 原始文件名
            
        Returns:
            str: 清理后的文件名
        """
        # 移除不安全字符
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        # 移除前后空格和点
        filename = filename.strip(' .')
        # 确保不为空
        if not filename:
            filename = "template"
        return filename