# CeneoScraper

## Struktura opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|||
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|||
|autor opinii|span.user-post__author-name|||
|rekomendacja|span.user-post__author-recomendation > em|||
|liczba gwiazdek|span.user-post__score-count|||
|treść opinii|div.user-post__text|||
|lista zalet|div\[class$="positives"\]~div.review-feature__item|||
|lista wad|div\[class$="negatives"\]~div.review-feature__item|||
|dla ilu osób przydatna|span\[id^="votes-yes"\]|||
|dla ilu osób nieprzydatna|span\[id^="votes-no"\]|||
|data wystawienia opinii|span.user-post__publlished > time:nth-child(1)["datetime"]|||
|data zakupu|span.user-post__publlished > time:nth-child(2)["datetime"]|||