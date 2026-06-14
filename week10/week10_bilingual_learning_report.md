# Week 10 Bilingual Learning Report
# 第 10 周双语学习报告

## 1. Source Files Reviewed
## 1. 已分析文件

**English:** This report reviews five Week 10 files: `Data_Analysis_and_Visualization.pdf`, `Seaborn_Data_Visualization_Lecture.pptx`, `Recap-Clustering_&_Regression.pptx`, `Linear_Polynomial_Regression.pptx`, and `salary-dataset.csv`.

**中文：** 本报告分析了 Week 10 文件夹中的五个文件：`Data_Analysis_and_Visualization.pdf`、`Seaborn_Data_Visualization_Lecture.pptx`、`Recap-Clustering_&_Regression.pptx`、`Linear_Polynomial_Regression.pptx` 和 `salary-dataset.csv`。

**English:** The materials focus on data visualization, Seaborn plotting, clustering review, regression concepts, and salary prediction using linear regression.

**中文：** 这些材料主要围绕数据可视化、Seaborn 绘图、聚类复习、回归概念，以及使用线性回归进行薪资预测。

**English:** The PDF has a weak text layer, so its content was reviewed through rendered page images rather than only extracted text.

**中文：** 该 PDF 的文本层较弱，因此分析时使用了页面渲染图进行视觉检查，而不是只依赖文本提取。

## 2. Overall Learning Theme
## 2. 总体学习主题

**English:** Week 10 connects descriptive analytics and predictive analytics.

**中文：** 第 10 周把描述性分析和预测性分析连接起来。

**English:** Visualization helps students explore patterns, clustering helps group similar observations, and regression helps predict a numerical outcome from one or more variables.

**中文：** 可视化帮助学生探索数据模式，聚类帮助把相似观察对象分组，回归帮助根据一个或多个变量预测数值结果。

**English:** The learning path moves from "What does the data look like?" to "Which groups exist?" and then to "What value can we predict?"

**中文：** 学习路径从“数据看起来是什么样？”过渡到“数据中有哪些群体？”，再到“我们可以预测什么数值？”。

## 3. Data Visualization and Seaborn
## 3. 数据可视化与 Seaborn

**English:** The PDF introduces the Python visualization stack: Matplotlib provides low-level plotting control, while Seaborn provides a higher-level statistical visualization interface.

**中文：** PDF 介绍了 Python 可视化工具栈：Matplotlib 提供底层绘图控制，而 Seaborn 提供更高层次的统计可视化接口。

**English:** Matplotlib plots are built from figures, axes, and artists, so students should understand the structure before customizing charts.

**中文：** Matplotlib 图表由 figure、axes 和 artists 组成，因此学生在自定义图表前应先理解这些结构。

**English:** A standard Matplotlib workflow is to create a figure and axes, plot the data, and then add labels, titles, and legends.

**中文：** 标准 Matplotlib 工作流程是先创建 figure 和 axes，再绘制数据，最后添加标签、标题和图例。

**English:** Seaborn is useful because it works naturally with pandas DataFrames, adds automatic statistical summaries, and provides cleaner default themes.

**中文：** Seaborn 的优势在于它能自然配合 pandas DataFrame，自动加入统计摘要，并提供更美观的默认主题。

**English:** The Seaborn lecture covers distribution plots, categorical plots, matrix plots, grid-based plots, regression plots, and styling controls.

**中文：** Seaborn 课件覆盖了分布图、分类图、矩阵图、网格图、回归图和样式控制。

## 4. Key Seaborn Plot Types
## 4. Seaborn 关键图表类型

**English:** Distribution plots such as `displot`, `kdeplot`, `rugplot`, `jointplot`, and `pairplot` help reveal spread, density, and relationships between variables.

**中文：** `displot`、`kdeplot`、`rugplot`、`jointplot` 和 `pairplot` 等分布图可以帮助观察变量的分布、密度和变量之间的关系。

**English:** Categorical plots such as `barplot`, `countplot`, `boxplot`, `violinplot`, `stripplot`, `swarmplot`, and `catplot` compare groups and expose category-level patterns.

**中文：** `barplot`、`countplot`、`boxplot`、`violinplot`、`stripplot`、`swarmplot` 和 `catplot` 等分类图用于比较群体，并展示类别层面的规律。

**English:** Matrix plots such as `heatmap` and `clustermap` are useful for correlation matrices, pivot tables, and similarity structures.

**中文：** `heatmap` 和 `clustermap` 等矩阵图适合展示相关矩阵、透视表和相似性结构。

**English:** Grid tools such as `PairGrid`, `FacetGrid`, and `JointGrid` allow the same plotting logic to be repeated across many variables or groups.

**中文：** `PairGrid`、`FacetGrid` 和 `JointGrid` 等网格工具可以把同一种绘图逻辑应用到多个变量或多个分组上。

**English:** Regression plots such as `lmplot` and `regplot` combine scatterplots with fitted trend lines, making relationships easier to interpret.

**中文：** `lmplot` 和 `regplot` 等回归图把散点图和拟合趋势线结合起来，使变量关系更容易解释。

## 5. Clustering Review
## 5. 聚类复习

**English:** The clustering recap emphasizes that clustering is an unsupervised method used to group similar observations.

**中文：** 聚类复习课件强调，聚类是一种无监督方法，用于把相似的观察对象分到同一组。

**English:** Good clustering depends heavily on selecting variables that match the research objective.

**中文：** 好的聚类结果高度依赖变量选择，而变量必须服务于研究目标。

**English:** Important design decisions include sample size, outlier detection, similarity measurement, standardization, and the number of clusters.

**中文：** 重要的研究设计决策包括样本量、异常值检测、相似度度量、标准化处理和聚类数量选择。

**English:** The slides distinguish hierarchical clustering, where observations are gradually joined, from non-hierarchical clustering, where the number of clusters is specified first.

**中文：** 课件区分了层次聚类和非层次聚类：层次聚类逐步合并观察对象，非层次聚类则先指定聚类数量。

**English:** Cluster solutions must be validated because clustering will always produce groups, even when the groups are not meaningful.

**中文：** 聚类结果必须验证，因为聚类算法总会生成分组，即使这些分组未必有实际意义。

## 6. Regression Concepts
## 6. 回归概念

**English:** Regression is a supervised learning approach used to model the relationship between a dependent variable and one or more independent variables.

**中文：** 回归是一种监督学习方法，用于建模因变量和一个或多个自变量之间的关系。

**English:** Simple linear regression uses one predictor, while multiple regression uses several predictors.

**中文：** 简单线性回归使用一个预测变量，多元回归使用多个预测变量。

**English:** Linear regression assumes a straight-line relationship and estimates an intercept and slope by minimizing squared prediction errors.

**中文：** 线性回归假设变量之间存在直线关系，并通过最小化平方预测误差来估计截距和斜率。

**English:** Polynomial regression extends linear regression by adding transformed features such as `x^2`, `x^3`, and higher-degree terms.

**中文：** 多项式回归通过加入 `x^2`、`x^3` 等高阶变换特征来扩展线性回归。

**English:** Polynomial regression can fit curved patterns, but a high polynomial degree can overfit the training data.

**中文：** 多项式回归可以拟合曲线模式，但过高的多项式阶数可能导致对训练数据过拟合。

## 7. Salary Dataset Analysis
## 7. 薪资数据集分析

**English:** The `salary-dataset.csv` file contains 36 records and three columns: an unnamed index column, `YearsExperience`, and `Salary`.

**中文：** `salary-dataset.csv` 包含 36 条记录和三列：一个未命名索引列、`YearsExperience` 和 `Salary`。

**English:** Years of experience range from 1.2 to 13.0 years, with an average of about 6.52 years.

**中文：** 工作经验范围从 1.2 年到 13.0 年，平均约为 6.52 年。

**English:** Salary ranges from 37,732 to 138,821, with an average salary of about 85,667.08.

**中文：** 薪资范围从 37,732 到 138,821，平均薪资约为 85,667.08。

**English:** A simple linear regression estimate gives a slope of about 9,063.48, meaning each additional year of experience is associated with roughly 9,063 more salary units.

**中文：** 简单线性回归估计的斜率约为 9,063.48，表示每增加一年工作经验，薪资大约增加 9,063 个单位。

**English:** The estimated intercept is about 26,553.08, which is the model's predicted salary when experience is zero.

**中文：** 估计截距约为 26,553.08，表示模型在工作经验为 0 时预测的薪资。

**English:** The correlation between years of experience and salary is very strong, with `r = 0.9861` and `R^2 = 0.9723`.

**中文：** 工作经验和薪资之间的相关性非常强，`r = 0.9861`，`R^2 = 0.9723`。

**English:** Based on this model, the predicted salary is about 71,870.46 for 5 years of experience and about 117,187.84 for 10 years of experience.

**中文：** 根据该模型，5 年工作经验的预测薪资约为 71,870.46，10 年工作经验的预测薪资约为 117,187.84。

## 8. Suggested Study Workflow
## 8. 建议学习流程

**English:** First, use Seaborn distribution and categorical plots to inspect the salary data visually.

**中文：** 第一步，使用 Seaborn 的分布图和分类图对薪资数据进行视觉探索。

**English:** Second, draw a scatterplot of `YearsExperience` versus `Salary` and add a regression line using `regplot` or `lmplot`.

**中文：** 第二步，绘制 `YearsExperience` 与 `Salary` 的散点图，并使用 `regplot` 或 `lmplot` 添加回归线。

**English:** Third, fit a linear regression model and interpret the slope, intercept, correlation, and `R^2`.

**中文：** 第三步，拟合线性回归模型，并解释斜率、截距、相关系数和 `R^2`。

**English:** Fourth, compare whether a polynomial model is necessary by checking if the scatterplot shows a curved pattern.

**中文：** 第四步，通过观察散点图是否呈现曲线模式，判断是否有必要使用多项式模型。

**English:** Finally, connect regression with clustering by asking how grouped user segments might have different prediction patterns.

**中文：** 最后，把回归和聚类联系起来，思考不同用户群体是否会呈现不同的预测模式。

## 9. Practice Tasks
## 9. 练习任务

**English:** Create a histogram and KDE plot for `Salary`.

**中文：** 为 `Salary` 创建直方图和 KDE 密度图。

**English:** Create a scatterplot of `YearsExperience` and `Salary`, then add a fitted regression line.

**中文：** 创建 `YearsExperience` 和 `Salary` 的散点图，并添加拟合回归线。

**English:** Train a simple linear regression model and report the equation in the form `Salary = intercept + slope * YearsExperience`.

**中文：** 训练一个简单线性回归模型，并用 `Salary = 截距 + 斜率 * YearsExperience` 的形式报告方程。

**English:** Compare linear and polynomial regression visually, then explain which model is more appropriate for this dataset.

**中文：** 通过可视化比较线性回归和多项式回归，然后解释哪个模型更适合该数据集。

**English:** Write a short conclusion explaining how visualization supports better modeling decisions.

**中文：** 写一个简短结论，说明可视化如何支持更好的建模决策。

## 10. Key Takeaway
## 10. 核心结论

**English:** Week 10 teaches that effective data analytics starts with visual exploration, becomes stronger through careful grouping and validation, and becomes actionable through regression-based prediction.

**中文：** 第 10 周的核心是：有效的数据分析始于可视化探索，通过谨慎分组和验证变得更可靠，并通过回归预测转化为可执行洞察。
