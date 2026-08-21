# Prakhar Tiwari | Data Science Portfolio

A personal portfolio website for data-science opportunities, with beginner-friendly projects in banking, financial services, insurance (BFSI), and U.S. healthcare wellbeing analytics.

> **Live site:** Add your GitHub Pages URL here after publishing: `https://YOUR-GITHUB-USERNAME.github.io`

## About

This portfolio is designed to show more than a list of tools. It highlights an end-to-end analytical approach: framing a practical problem, preparing data, building a reproducible analysis or model, evaluating it appropriately, and communicating a useful outcome.

The site is built from the responsive **Editorial** template by HTML5 UP and is ready to deploy through GitHub Pages.

## Featured projects

| Project | Domain | Business question | Main skills |
| --- | --- | --- | --- |
| [Card Fraud Detection](projects/fraud-detection/README.md) | BFSI | Which transactions should be prioritized for fraud-analyst review? | Imbalanced classification, PR-AUC, precision/recall, risk ranking |
| [Bank Customer Segmentation](projects/bank-customer-segmentation/README.md) | BFSI | What broad engagement patterns appear in the customer base? | Clustering, scaling, silhouette score, segment profiling |
| [U.S. Wellbeing Trends Dashboard](projects/us-wellbeing-dashboard/README.md) | Healthcare | How do population-level wellbeing indicators vary by state and over time? | Public-health analytics, Streamlit, Plotly, descriptive visualization |

Each project folder includes:

- A concise business-problem statement
- Public dataset guidance
- Runnable Python code and dependencies
- A real-world application and an interview-ready talking point

## Technology

- **Website:** HTML5, CSS3, JavaScript
- **Data work:** Python, pandas, scikit-learn
- **Visualization:** Streamlit, Plotly
- **Version control and hosting:** GitHub and GitHub Pages

## Project structure

```text
.
├── index.html                         # Portfolio homepage
├── assets/                            # Template styles, scripts, and fonts
├── images/                            # Website images
└── projects/
    ├── fraud-detection/               # BFSI classification project
    ├── bank-customer-segmentation/    # BFSI clustering project
    └── us-wellbeing-dashboard/        # U.S. healthcare dashboard
```

## Run the website locally

The website is static. Open `index.html` in a browser to preview it, or use any simple local web server.

## Run a data project

Each project has its own setup instructions. As an example:

```bash
cd projects/fraud-detection
pip install -r requirements.txt
python train.py --data data/creditcard.csv
```

Download the recommended public dataset first and save it at the path stated in that project’s README. Dataset files and generated outputs are intentionally not included in this repository.

## Publish with GitHub Pages

1. Create a public repository named `YOUR-GITHUB-USERNAME.github.io`.
2. Upload this project’s files and folders, including `index.html`, `assets`, `images`, and `projects`.
3. In GitHub, go to **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select the `main` branch and the root (`/`) folder, then save.
6. GitHub will publish the site at `https://YOUR-GITHUB-USERNAME.github.io`.

## Customize before publishing

Update these items in `index.html`:

- `YOUR_EMAIL@example.com`
- `YOUR_CITY, YOUR_COUNTRY`
- Your GitHub profile link
- Project cards with your actual results, screenshots, and repository links after you run each project

Avoid adding metrics you have not personally produced. A concise, accurate result is more credible than an impressive-sounding claim without evidence.

## Responsible use note

The BFSI projects are learning demonstrations. Fraud scores should support human review, not automatic account actions. Customer segments should not be used for credit eligibility, pricing, or other decisions that restrict access to financial services.

The wellbeing dashboard uses aggregate public-health indicators only. It is not a clinical tool and must not be used for individual diagnosis or treatment decisions.

## License and credits

The underlying Editorial website design is by [HTML5 UP](https://html5up.net) and is licensed under the [Creative Commons Attribution 3.0 License](https://html5up.net/license). See `LICENSE.txt` for details.
