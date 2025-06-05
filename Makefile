# FIVC项目Makefile - 使用uv进行包管理

.PHONY: help install install-dev test test-cov lint format clean build publish
.DEFAULT_GOAL := help

# 颜色定义
BLUE := \033[36m
GREEN := \033[32m
YELLOW := \033[33m
RED := \033[31m
NC := \033[0m # No Color

help: ## 显示帮助信息
	@echo "$(BLUE)FIVC项目可用命令:$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

install: ## 安装项目依赖
	@echo "$(BLUE)安装项目依赖...$(NC)"
	uv pip install -e .

install-dev: ## 安装开发依赖
	@echo "$(BLUE)安装开发依赖...$(NC)"
	uv pip install -e ".[dev,test]"

install-all: ## 安装所有依赖（包括可选依赖）
	@echo "$(BLUE)安装所有依赖...$(NC)"
	uv pip install -e ".[all]"

test: ## 运行测试
	@echo "$(BLUE)运行测试...$(NC)"
	pytest tests/ -v

test-cov: ## 运行测试并生成覆盖率报告
	@echo "$(BLUE)运行测试并生成覆盖率报告...$(NC)"
	pytest --cov=fivc --cov-report=term-missing --cov-report=html tests/

test-fast: ## 快速测试（跳过慢速测试）
	@echo "$(BLUE)快速测试...$(NC)"
	pytest tests/ -v -m "not slow"

lint: ## 运行代码检查
	@echo "$(BLUE)运行代码检查...$(NC)"
	@echo "$(YELLOW)运行ruff检查...$(NC)"
	ruff check .
	@echo "$(YELLOW)运行black检查...$(NC)"
	black --check --diff .
	@echo "$(YELLOW)运行isort检查...$(NC)"
	isort --check-only --diff .
	@echo "$(YELLOW)运行mypy类型检查...$(NC)"
	mypy --install-types --non-interactive src/fivc tests

format: ## 格式化代码
	@echo "$(BLUE)格式化代码...$(NC)"
	@echo "$(YELLOW)运行isort...$(NC)"
	isort .
	@echo "$(YELLOW)运行black...$(NC)"
	black .
	@echo "$(YELLOW)运行ruff修复...$(NC)"
	ruff check --fix .

clean: ## 清理构建文件和缓存
	@echo "$(BLUE)清理构建文件和缓存...$(NC)"
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: clean ## 构建项目
	@echo "$(BLUE)构建项目...$(NC)"
	python -m build

build-uv: clean ## 使用uv构建项目
	@echo "$(BLUE)使用uv构建项目...$(NC)"
	uv build

publish-test: build ## 发布到测试PyPI
	@echo "$(BLUE)发布到测试PyPI...$(NC)"
	python -m twine upload --repository testpypi dist/*

publish: build ## 发布到PyPI
	@echo "$(RED)发布到PyPI...$(NC)"
	@echo "$(YELLOW)确认要发布到生产环境？[y/N]$(NC)"
	@read -r REPLY; \
	if [ "$$REPLY" = "y" ] || [ "$$REPLY" = "Y" ]; then \
		python -m twine upload dist/*; \
	else \
		echo "取消发布"; \
	fi

venv: ## 创建虚拟环境
	@echo "$(BLUE)使用uv创建虚拟环境...$(NC)"
	uv venv
	@echo "$(GREEN)虚拟环境已创建，激活方式：$(NC)"
	@echo "$(YELLOW)source .venv/bin/activate$(NC)  # Linux/macOS"
	@echo "$(YELLOW).venv\\Scripts\\activate$(NC)      # Windows"

sync: ## 同步依赖（使用uv）
	@echo "$(BLUE)同步依赖...$(NC)"
	uv pip sync

lock: ## 生成锁定文件
	@echo "$(BLUE)生成锁定文件...$(NC)"
	uv pip freeze > requirements.lock

check: ## 检查项目配置
	@echo "$(BLUE)检查项目配置...$(NC)"
	python -m build --check

dev-setup: venv install-dev ## 完整开发环境设置
	@echo "$(GREEN)开发环境设置完成！$(NC)"
	@echo "$(YELLOW)接下来运行以下命令激活环境：$(NC)"
	@echo "source .venv/bin/activate  # Linux/macOS"
	@echo ".venv\\Scripts\\activate      # Windows"

pre-commit-install: ## 安装pre-commit钩子
	@echo "$(BLUE)安装pre-commit钩子...$(NC)"
	pre-commit install

pre-commit-run: ## 运行pre-commit检查
	@echo "$(BLUE)运行pre-commit检查...$(NC)"
	pre-commit run --all-files

info: ## 显示项目信息
	@echo "$(BLUE)项目信息:$(NC)"
	@echo "名称: FIVC (Five Component Framework)"
	@echo "版本: $(shell python -c 'from src.fivc.__about__ import __version__; print(__version__)')"
	@echo "Python版本要求: >=3.8"
	@echo "构建系统: hatchling + uv" 