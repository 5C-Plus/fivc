# FIVC 开发指南

本文档提供 FIVC 项目的开发环境设置和开发流程指南。

## 🚀 快速开始

### 环境要求

- Python 3.8+
- uv (推荐) 或 pip
- Git

### 环境设置

#### 使用 uv（推荐）

```bash
# 克隆仓库
git clone https://github.com/5C-Plus/fivc.git
cd fivc

# 安装 uv（如果尚未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 创建虚拟环境并安装开发依赖
uv venv
uv sync --all-extras

# 激活虚拟环境
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

#### 传统方式

```bash
# 克隆仓库
git clone https://github.com/5C-Plus/fivc.git
cd fivc

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -e ".[dev,test]"
```

## 🧪 运行测试

### 使用 uv

```bash
# 运行所有测试
uv run pytest tests/

# 运行特定测试
uv run pytest tests/test_configs.py

# 运行测试并生成覆盖率报告
uv run pytest --cov=fivc --cov-report=html tests/

# 运行测试并要求最低覆盖率
uv run pytest tests/ -v --cov-fail-under=75
```

### 测试覆盖率

项目要求测试覆盖率不低于 75%。当前覆盖率约为 82%。

## 🔧 代码检查和格式化

### 使用 Ruff

```bash
# 代码检查
uv run ruff check .

# 自动修复问题
uv run ruff check --fix .

# 代码格式化
uv run ruff format .
```

### 类型检查

```bash
# 运行 MyPy 类型检查
uv run mypy --install-types --non-interactive src/fivc tests
```

## 🏗️ 构建项目

### 使用 uv

```bash
# 清理旧的构建文件
Remove-Item -Recurse -Force dist -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force build -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force *.egg-info -ErrorAction SilentlyContinue

# 构建项目
uv build

# 检查构建结果
ls dist/
```

### 验证构建

```bash
# 安装构建的包
uv pip install --force-reinstall dist/fivc-*.whl

# 测试安装
uv run python -c "import fivc; print('FIVC version:', fivc.__version__)"
```

## 📁 项目结构

```
fivc/
├── src/fivc/           # 主要源代码
│   ├── core/           # 核心模块
│   │   ├── interfaces/ # 接口定义
│   │   ├── implements/ # 接口实现
│   │   └── fixtures/   # 测试夹具
│   ├── __about__.py    # 版本信息
│   └── cli.py          # 命令行接口
├── tests/              # 测试代码
├── scripts/            # 脚本工具
├── fixtures/           # 测试数据
├── docs/               # 项目文档
├── pyproject.toml      # 项目配置
├── ruff.toml           # Ruff 配置
└── uv.lock             # uv 锁定文件
```

## 📝 开发规范

### 代码风格

- 遵循 PEP 8 代码风格规范
- 使用类型注解 (Type Hints)
- 优先使用 `from __future__ import annotations` 进行延迟注解
- 函数和类必须有文档字符串
- 行长度限制为 100 字符

### 命名规范

- 类名：使用 PascalCase (如 `ComponentSite`)
- 函数名：使用 snake_case (如 `get_component`)
- 常量：使用 UPPER_SNAKE_CASE (如 `DEFAULT_CONFIG`)
- 接口类：以 `I` 开头 (如 `IComponent`, `IConfig`)
- 私有成员：以单下划线开头 (如 `_private_method`)

### 导入规范

```python
# 标准库导入
import os
from abc import ABCMeta, abstractmethod
from typing import TextIO

# 第三方库导入
import yaml

# 本地导入
from fivc.core.interfaces import IComponent
```

## 🧪 测试规范

### 测试文件命名

- 测试文件以 `test_` 开头
- 测试类以 `Test` 开头
- 测试方法以 `test_` 开头

### 测试结构

```python
import unittest
from fivc.core.implements.utils import load_component_site
from fivc.core.interfaces.utils import query_component

class TestComponentName(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 类级别的设置
        pass
    
    def test_specific_functionality(self):
        # 具体功能测试
        pass
```

## 🚀 发布流程

### 发布前检查

```bash
# 运行发布检查脚本
uv run python scripts/check_release.py
```

### 构建和发布

```bash
# 构建项目
uv build

# 发布到 PyPI（需要 API token）
uv publish --token <your-pypi-token>

# 或使用用户名密码
uv publish -u <username> -p <password>
```

## 🤝 贡献流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 进行开发并编写测试
4. 运行代码检查：`uv run ruff check --fix .`
5. 运行测试：`uv run pytest tests/ -v --cov-fail-under=75`
6. 提交更改 (`git commit -m 'Add some amazing feature'`)
7. 推送到分支 (`git push origin feature/amazing-feature`)
8. 开启 Pull Request

### Git 提交规范

```
type(scope): description

[optional body]

[optional footer]
```

提交类型：
- `feat`: 新功能
- `fix`: 错误修复
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

## 🔧 常用命令

```bash
# 开发环境设置
uv venv && uv sync

# 运行测试
uv run pytest tests/ -v

# 代码检查和格式化
uv run ruff check --fix . && uv run ruff format .

# 构建项目
uv build

# 发布检查
uv run python scripts/check_release.py
```

## 📞 获取帮助

- **GitHub Issues**: 报告问题和功能请求
- **讨论区**: 技术讨论和经验分享
- **邮件**: sunnypig2002@gmail.com

---

*最后更新: 2024年* 