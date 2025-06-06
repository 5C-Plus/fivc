# FIVC - Five Component Framework

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Development Status](https://img.shields.io/badge/development-beta-orange.svg)](https://github.com/5C-Plus/fivc)

FIVC 是一个轻量级的 Python 组件管理框架，提供了灵活的组件注册、查询和依赖注入机制。

## 📚 文档

- [📋 完整文档](docs/README.md) - 项目文档中心
- [🚀 发布说明](docs/RELEASE_NOTES.md) - 版本发布说明
- [📖 发布准备](docs/PUBLISH_READY.md) - 发布检查清单
- [🔧 开发指南](docs/DEVELOPMENT.md) - 开发环境和流程

## 特性

- 🔧 **组件接口抽象**: 基于抽象基类的组件接口定义
- 🔌 **依赖注入**: 灵活的组件注册和查询机制
- 📁 **配置管理**: 支持 JSON 和 YAML 格式的配置文件
- 🗄️ **缓存系统**: 内置内存和 Redis 缓存支持
- 📝 **日志系统**: 内置日志组件
- 🔒 **互斥锁**: 分布式锁支持
- 🎯 **类型安全**: 完整的类型注解支持

## 安装

### 使用 pip 安装

```bash
pip install fivc
```

### 使用 uv 安装（推荐）

```bash
# 安装 uv（如果尚未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 安装 FIVC
uv add fivc
```

## 快速开始

```python
from fivc.core import IComponent, IComponentSite
from fivc.core.implements.utils import load_component_site
from fivc.core.interfaces.utils import query_component

# 加载组件站点
component_site = load_component_site(fmt="yaml")

# 查询组件
config = query_component(component_site, IConfig, "Json")
if config:
    session = config.get_session("app")
    value = session.get_value("database_url")
```

## 核心组件

### 配置管理
- `IConfig`: 配置接口
- `JsonFileConfig`: JSON 文件配置实现
- `YamlFileConfig`: YAML 文件配置实现

### 缓存系统
- `ICache`: 缓存接口
- `MemoryCache`: 内存缓存实现
- `RedisCache`: Redis 缓存实现

### 日志系统
- `ILogger`: 日志接口
- `BuiltinLogger`: 内置日志实现

### 互斥锁
- `IMutex`: 互斥锁接口
- `RedisMutex`: Redis 分布式锁实现

## 开发

详细的开发指南请参考 [开发文档](docs/DEVELOPMENT.md)。

### 快速开发环境设置

```bash
# 克隆仓库
git clone https://github.com/5C-Plus/fivc.git
cd fivc

# 使用 uv 设置环境
uv venv && uv sync

# 运行测试
uv run pytest tests/ -v --cov-fail-under=75
```

## 项目结构

```
fivc/
├── src/fivc/           # 主要源代码
│   ├── core/           # 核心模块
│   │   ├── interfaces/ # 接口定义
│   │   ├── implements/ # 接口实现
│   │   └── fixtures/   # 测试夹具
│   └── __about__.py    # 版本信息
├── tests/              # 测试代码
├── docs/               # 项目文档
├── scripts/            # 脚本工具
├── fixtures/           # 测试数据
├── pyproject.toml      # 项目配置
└── ruff.toml           # 代码检查配置
```

## 贡献

欢迎贡献代码！请查看 [开发指南](docs/DEVELOPMENT.md) 了解详细的贡献流程。

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](LICENSE) 文件。

## 作者

- **Charlie ZHANG** - *初始工作* - [sunnypig2002@gmail.com](mailto:sunnypig2002@gmail.com)

## 链接

- [📚 项目文档](docs/README.md)
- [🐛 问题反馈](https://github.com/5C-Plus/fivc/issues)
- [💻 源代码](https://github.com/5C-Plus/fivc)