# -*- coding: utf-8 -*-
"""
文件操作工具模块
提供文件和目录操作的通用功能
"""

import os
import shutil
import json
from pathlib import Path
from typing import Dict, Any, Optional


def ensure_dir(path: str) -> None:
    """确保目录存在
    
    Args:
        path: 目录路径
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def copy_file(src: str, dst: str) -> None:
    """复制文件
    
    Args:
        src: 源文件路径
        dst: 目标文件路径
    """
    ensure_dir(os.path.dirname(dst))
    shutil.copy2(src, dst)


def copy_directory(src: str, dst: str) -> None:
    """复制目录
    
    Args:
        src: 源目录路径
        dst: 目标目录路径
    """
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def remove_file(path: str) -> None:
    """删除文件
    
    Args:
        path: 文件路径
    """
    if os.path.exists(path):
        os.remove(path)


def remove_directory(path: str) -> None:
    """删除目录
    
    Args:
        path: 目录路径
    """
    if os.path.exists(path):
        shutil.rmtree(path)


def read_file(path: str, encoding: str = 'utf-8') -> str:
    """读取文件内容
    
    Args:
        path: 文件路径
        encoding: 文件编码
        
    Returns:
        str: 文件内容
    """
    with open(path, 'r', encoding=encoding) as f:
        return f.read()


def write_file(path: str, content: str, encoding: str = 'utf-8') -> None:
    """写入文件内容
    
    Args:
        path: 文件路径
        content: 文件内容
        encoding: 文件编码
    """
    ensure_dir(os.path.dirname(path))
    with open(path, 'w', encoding=encoding) as f:
        f.write(content)


def read_json(path: str) -> Dict[str, Any]:
    """读取JSON文件
    
    Args:
        path: JSON文件路径
        
    Returns:
        Dict[str, Any]: JSON数据
    """
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(path: str, data: Dict[str, Any], indent: int = 2) -> None:
    """写入JSON文件
    
    Args:
        path: JSON文件路径
        data: JSON数据
        indent: 缩进空格数
    """
    ensure_dir(os.path.dirname(path))
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def get_file_size(path: str) -> int:
    """获取文件大小
    
    Args:
        path: 文件路径
        
    Returns:
        int: 文件大小（字节）
    """
    return os.path.getsize(path)


def file_exists(path: str) -> bool:
    """检查文件是否存在
    
    Args:
        path: 文件路径
        
    Returns:
        bool: 文件是否存在
    """
    return os.path.isfile(path)


def dir_exists(path: str) -> bool:
    """检查目录是否存在
    
    Args:
        path: 目录路径
        
    Returns:
        bool: 目录是否存在
    """
    return os.path.isdir(path)


def list_files(directory: str, pattern: str = '*') -> list:
    """列出目录下的文件
    
    Args:
        directory: 目录路径
        pattern: 文件匹配模式
        
    Returns:
        list: 文件路径列表
    """
    path = Path(directory)
    return [str(f) for f in path.glob(pattern) if f.is_file()]


def list_directories(directory: str) -> list:
    """列出目录下的子目录
    
    Args:
        directory: 目录路径
        
    Returns:
        list: 子目录路径列表
    """
    path = Path(directory)
    return [str(d) for d in path.iterdir() if d.is_dir()]


def get_relative_path(path: str, base: str) -> str:
    """获取相对路径
    
    Args:
        path: 目标路径
        base: 基础路径
        
    Returns:
        str: 相对路径
    """
    return os.path.relpath(path, base)


def join_path(*paths: str) -> str:
    """连接路径
    
    Args:
        *paths: 路径组件
        
    Returns:
        str: 连接后的路径
    """
    return os.path.join(*paths)


def get_file_extension(path: str) -> str:
    """获取文件扩展名
    
    Args:
        path: 文件路径
        
    Returns:
        str: 文件扩展名
    """
    return os.path.splitext(path)[1]


def get_filename_without_extension(path: str) -> str:
    """获取不带扩展名的文件名
    
    Args:
        path: 文件路径
        
    Returns:
        str: 不带扩展名的文件名
    """
    return os.path.splitext(os.path.basename(path))[0]