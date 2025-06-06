# FIVC v0.1.0 发布说明

## 📦 版本信息
- **版本号**: 0.1.0
- **发布日期**: 2024年
- **Python支持**: 3.8+

## 🎉 新特性

### 核心框架
- ✅ **轻量级组件管理框架**: 提供完整的组件注册、查询和依赖注入机制
- ✅ **接口设计模式**: 基于抽象基类的接口定义，支持多实现
- ✅ **组件站点 (ComponentSite)**: 统一的组件管理容器
- ✅ **依赖注入**: 自动化的组件查询和注入机制

### 配置管理
- ✅ **多格式支持**: 支持 JSON 和 YAML 配置文件
- ✅ **灵活配置**: 支持文件路径配置和环境变量
- ✅ **配置组件**: `IConfig` 接口及其实现

### 缓存系统
- ✅ **内存缓存**: 基于字典的高速内存缓存实现
- ✅ **Redis缓存**: 分布式Redis缓存支持，包含连接池和自动序列化
- ✅ **TTL支持**: 完整的过期时间管理
- ✅ **二进制数据**: 支持任意Python对象的序列化存储

### 日志系统
- ✅ **内置日志**: 基于Python标准库的日志实现
- ✅ **日志站点**: `ILoggerSite` 接口管理多个日志器
- ✅ **灵活配置**: 支持不同级别和格式的日志输出

## 🏗️ 架构特点

### 设计模式
- **依赖注入容器**: 统一管理所有组件
- **接口隔离**: 清晰的接口和实现分离
- **工厂模式**: 组件构建器支持灵活的实例化
- **策略模式**: 多种缓存和配置策略

### 代码质量
- **类型注解**: 完整的TypeScript风格类型提示
- **文档字符串**: 详细的API文档
- **测试覆盖**: 82%的代码覆盖率
- **PEP 8**: 符合Python代码规范

## 📂 包结构

```
fivc/
├── __init__.py              # 主入口模块
├── __about__.py             # 版本和元数据
└── core/                    # 核心框架
    ├── __init__.py
    ├── interfaces/          # 接口定义
    │   ├── caches.py       # 缓存接口
    │   ├── configs.py      # 配置接口
    │   ├── loggers.py      # 日志接口
    │   └── utils.py        # 工具接口
    ├── implements/          # 接口实现
    │   ├── caches_mem.py   # 内存缓存
    │   ├── caches_redis.py # Redis缓存
    │   ├── configs_*.py    # 配置实现
    │   ├── loggers_*.py    # 日志实现
    │   └── utils.py        # 工具实现
    └── fixtures/            # 默认配置
        └── configs_basics.yml
```

## 🚀 快速开始

### 安装
```bash
pip install fivc
```

### 基本使用
```python
import fivc

# 使用默认配置
component_site = fivc.component_site

# 获取缓存组件
from fivc.core.interfaces import caches
cache = component_site.query_component(caches.ICache, "Memory")

# 缓存操作
cache.set_value("key", "value", ttl=300)
value = cache.get_value("key")
```

### 自定义配置
```python
from fivc.core.implements.utils import load_component_site

# 加载自定义配置
site = load_component_site("my_config.yml", fmt="yml")
```

## 📋 依赖项
- **PyYAML**: YAML配置文件支持
- **Redis**: Redis缓存支持（可选）

## 🧪 测试结果
- ✅ **测试通过**: 7/7 测试用例
- ✅ **代码覆盖**: 82%
- ✅ **类型检查**: MyPy验证通过
- ✅ **包完整性**: Wheel文件验证通过

## 📖 文档
- 完整的API文档和类型注解
- 详细的使用示例
- 架构设计说明

## 🔄 升级说明
这是首个公开版本，无升级兼容性问题。

## 🐛 已知问题
无已知重大问题。

## 🤝 贡献
欢迎提交Issue和Pull Request。

## 📄 许可证
MIT License

## 🔗 相关链接
- **PyPI**: https://pypi.org/project/fivc/
- **GitHub**: (项目地址)
- **文档**: (文档地址)

---

**感谢使用 FIVC！** 🎉 