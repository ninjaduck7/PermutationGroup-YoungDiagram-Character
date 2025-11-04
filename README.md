
# 置换群S_n不可约表示特征标计算与可视化

> **北京理工大学 物理学院 · 2025级**  
> **TJM** — 核心数学框架（Main Contributor）  
> **ZYF** — 网页构建与可视化（Web Implementation）

---

## 📘 项目简介

本项目以置换群 $S_n$ 为例，实现了其不可约表示的**特征标（Character）计算与可视化展示**。  
同时提供两种形式：

1. 🧮 **Python 实现** — 在 `Sn_IrrepChar.py` 中完成符号化算法；
2. 🌐 **网页交互版** — [在线可交互演示（Sn_IrrepChar.html）](https://ninjaduck7.github.io/PermutationGroup-YoungDiagram-Character)，以 Young 图为核心的图形化可视化计算平台。


---

## 🧩 文件结构

```

Permutation_group/
│
├─ Sn_IrrepChar.html      # 网页端可视化交互程序（含数学讲解 + 图形规则）
├─ Sn_IrrepChar.py        # Python 脚本版计算实现
└─ snake.png              # 蛇形填充示意图（网页使用）

````

---

## 🌐 网页版说明（Sn_IrrepChar.html）

### 功能
- 提供置换群不可约表示特征标的**交互式可视化演示**；
- 支持输入配分 $\lambda$ 与循环结构，自动生成 Young 图；
- 自动计算每种合法填充的符号，并求得总体特征标；
- 内含规则解释与教学引导。

### 使用方法
1. 打开浏览器进入网页文件（或使用 VSCode + Live Server 打开 `Sn_IrrepChar.html`）；  
2. 输入参数，例如：
   - 配分 λ: `3,2,2`
   - 循环长度序列: `1,2,2,2`
3. 点击 **“计算 χ<sup>λ</sup>(C)”**，即可显示：
   - Young 图的可视化；
   - 所有合法填充；
   - 特征标数值结果。

---

## 🧮 Python 版说明（Sn_IrrepChar.py）

### 功能
- 实现了基于 “蛇形填充规则” 的特征标计算；
- 可直接用于符号验证与算法测试。

### 用法示例

```python
from Sn_IrrepChar import compute_irrep_character

partition = [3, 2, 2]
cycle_type = [1, 2, 2, 2]

chi = compute_irrep_character(partition, cycle_type)
print("χ^λ(C) =", chi)
````

输出：

```
χ^[3,2,2]((1^1 2^3)) = 1
```

---

## 🧠 理论背景

* 置换群 ( $S_n$ ) 的每个不可约表示可由 **配分（Partition）** 唯一标识；
* 对应的 **Young 图 / Young 表** 体现表示的对称性；

* 该方法对应于 Frobenius–Young 表示论框架的图形化实现。

---

## 📜 署名与许可

* **作者：**

  * TJM — 核心数学逻辑与符号计算框架
  * ZYF — 前端网页搭建与可视化设计
* **指导单位：** 北京理工大学 物理学院
* **许可证：** MIT License
* **版权年份：** © 2025

---

## 💡 致学习者

> 本项目旨在帮助物理与数学专业学生，以**可视化与符号结合的方式**理解置换群表示的结构。
> 你可以通过修改输入参数快速探索不同配分下的表示维度与特征标分布。




