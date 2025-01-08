# 纬度和经度识别模块

简体中文 | [English](./README.md)

本项目利用 **GADM（地理行政边界数据库）** 根据纬度和经度坐标识别所属的国家或地区。GADM 数据库定义了 400,276 个行政区域。

## GADM 数据库

- **当前版本**: 4.1
- **行政区域数量**: 400,276
- **下载链接**: [https://geodata.ucdavis.edu/gadm/gadm4.1/gadm_410-gpkg.zip](https://geodata.ucdavis.edu/gadm/gadm4.1/gadm_410-gpkg.zip)

---

## 使用方法

### 1. 下载数据库
确保已下载并将GADM数据库解压到项目根目录<br>
https://geodata.ucdavis.edu/gadm/gadm4.1/gadm_410-gpkg.zip

### 2. 安装依赖

确保已安装以下 Python 包：

```bash
pip install geopandas shapely pandas
```

### 3. 运行脚本

使用以下命令处理输入的 Excel 文件：

```bash
python process_excel.py <输入的Excel文件>
```

其中，`<输入的Excel文件>` 为包含纬度和经度列（`high_conf_lat` 和 `high_conf_lon`）的 Excel 文件路径。程序将输出一个新的 Excel 文件，并添加一列显示识别的区域。

---
