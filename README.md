# stockbot #

![build workflow](https://github.com/tanlin2013/stockbot/actions/workflows/build.yml/badge.svg)
![test workflow](https://github.com/tanlin2013/stockbot/actions/workflows/test.yml/badge.svg)

This is a research program aims at autonomous stock trading,
mainly focuses on Taiwanese stock market,
[TWSE](https://www.twse.com.tw/zh/).

### Introduction ###


### Get started ###

#### 1. Dependencies ####

  * [Shioaji](https://sinotrade.github.io/) (sinotrade's trading API)
  * [yfinance](https://github.com/ranaroussi/yfinance) (for downloading open data from yahoo finance)
  * [pandas-ta](https://github.com/twopirllc/pandas-ta) (technical indicators with pandas)

  See `requirements.txt` for details.

#### 2. Installation ####

  - using pip:

    ```
    pip install git+https://github.com/tanlin2013/stockbot@main
    ```
    
  - using Docker container (required to build from source):
    
    ```
    make build & make run 
    ```

#### 3. Tutorials ####

### Documentation ###
For details about stockbot,
see the [reference documentation](tanlin2013.github.io/stockbot/).

### Disclaimer ###

* All investments involve risk,
  and the past performance of a security, industry, sector, market, financial product, trading strategy, or individual’s trading does not guarantee future results or returns.
  Investors are fully responsible for any investment decisions they make.
  Such decisions should be based solely on an evaluation of their financial circumstances, investment objectives, risk tolerance, and liquidity needs.

* Any opinions, news, research, analyses, prices, or other information offered is provided as general market commentary, and does not constitute investment advice.
  I will not accept liability for any loss or damage,
  including without limitation any loss of profit,
  which may arise directly or indirectly from use of or reliance on such information.