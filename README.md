 <div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>39TH-SCHOOL-CCC</h1>
<h3>◦ Crafting Code with Class at 39th CCC!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python" />
</p>
<img src="https://img.shields.io/github/license/FilipJaskovic/39th-School-CCC?style=flat&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/FilipJaskovic/39th-School-CCC?style=flat&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/FilipJaskovic/39th-School-CCC?style=flat&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/FilipJaskovic/39th-School-CCC?style=flat&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The repository contains Python scripts designed to solve complex numerical problems related to currency transactions and numerical pairings. Key functionalities include optimizing currency denominations for transactions to minimize coin usage, finding pairs of numbers that sum up to predefined targets, and identifying missing integers within specified ranges. These solutions are intended for challenges where efficiency in numerical computation and output formatting is critical, delivering structured outputs to specified files, thereby automating part of the data processing and analysis tasks in financial and analytical scenarios. This provides a streamlined approach to handling specific types of numerical data operations.

---




## 📂 Repository Structure

```sh
└── 39th-School-CCC/
    ├── file-1-prod.py
    ├── file-2-prod.py
    ├── level-3.py
    └── level-4.py

```

---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [level-4.py](https://github.com/FilipJaskovic/39th-School-CCC/blob/main/level-4.py)         | The script reads input from a file named "level4_example.in" and processes sets of currency denominations along with transaction amounts. It separates the first two numbers and interprets subsequent lines as alternating lists of currencies and amounts. For each amount, the script calculates how it can be divided using the provided currencies in descending order, minimizing coin usage. Results for each transaction are aggregated into a formatted string capturing the breakdown of amounts into currency denominations. The final output is written to a file named "final_output2.txt", capturing the conversions for each amount separately. |
| [file-2-prod.py](https://github.com/FilipJaskovic/39th-School-CCC/blob/main/file-2-prod.py) | The code reads and processes a file to find pairs of numbers that sum up to target amounts from a predefined list. It opens "level2_5.in" to read numeric data, then parses and stores this data into arrays, initially splitting on new lines. The algorithm checks every combination of two numbers within each list against each target amount. Successful pairs, those that sum up to the target, are stored. Finally, these pairs are written to "output5.txt", formatted as a space-separated string on new lines.                                                                                                                                       |
| [file-1-prod.py](https://github.com/FilipJaskovic/39th-School-CCC/blob/main/file-1-prod.py) | The script in `file-1-prod.py` reads numbers from a file named `level1_5.in`, processes them, and outputs to `output5.txt`. It extracts the first three integers individually and subsequently processes remaining lines, treating each as a list of integers. For each list, the script identifies the first and the last number as minimum and maximum boundaries. It then writes the first missing integer within this range (if any) to `output5.txt`.                                                                                                                                                                                                     |
| [level-3.py](https://github.com/FilipJaskovic/39th-School-CCC/blob/main/level-3.py)         | The code defines a function `generate_amounts` in `level-3.py`, which calculates the minimum coin combinations needed to make target amounts from 1 to 100 using given coin denominations. It then reads a list of coin sets from a file `level3_5.in` and computes these combinations for each set. The results, formatted as count and denomination (e.g., "2x50"), are written to `output5.txt`. The function employs a dynamic programming approach to find the optimal coin combinations for each target amount.                                                                                                                                          |

</details>

---

## 🚀 Getting Started


### 🔧 Installation

1. Clone the 39th-School-CCC repository:
```sh
git clone https://github.com/FilipJaskovic/39th-School-CCC
```

2. Change to the project directory:
```sh
cd 39th-School-CCC
```


### 🤖 Running 39th-School-CCC

```sh
python main.py
```


---



---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/FilipJaskovic/39th-School-CCC/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/FilipJaskovic/39th-School-CCC/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/FilipJaskovic/39th-School-CCC/issues)**: Submit bugs found or log feature requests for FILIPJASKOVIC.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License


This project is protected under the [MIT](LICENSE) License. For more details, refer to the [LICENSE](LICENSE) file.

---

## 👏 Acknowledgments

- Jakub Jurčík, Elias Bauer

[**Return**](#Top)

---


