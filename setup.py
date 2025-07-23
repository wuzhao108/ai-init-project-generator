from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ai-init-project-generator",
    version="3.1.0",
    author="AI Assistant",
    author_email="ai@example.com",
    description="Java项目上下文工程生成器 - 智能生成Spring Boot项目初始化上下文提示词",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/ai-init-project-generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ai-init-generator=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "scripts": ["templates/**/*", "validators/**/*"],
    },
)