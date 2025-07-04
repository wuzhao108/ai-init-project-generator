
"""
Spring Boot项
一个基于Python的CLI命令行工具, 用于自动生成标准化的Java Spring Boot项目.
"""

__version__ = "1.0.0"
__author__ = "AI Assistant"
__email__ = "ai@example.com"

from .cli import cli
from .generator import ProjectGenerator
from .config import ProjectConfig, TechStack, ModuleConfig
from .interactive import InteractiveConfig

__all__ = [
    'cli',
    'ProjectGenerator',
    'ProjectConfig',
    'TechStack',
    'ModuleConfig',
    'InteractiveConfig'
]