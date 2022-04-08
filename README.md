# CeneoScraper

## Struktura opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion||
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id||
|autor opinii|span.user-post__author-name|author||
|rekomendacja|span.user-post__author-recomendation > em|recommendation||
|liczba gwiazdek|span.user-post__score-count|stars||
|treść opinii|div.user-post__text|content||
|lista zalet|div\[class$="positives"\]~div.review-feature__item|pros||
|lista wad|div\[class$="negatives"\]~div.review-feature__item|cons||
|dla ilu osób przydatna|span\[id^="votes-yes"\]|useful||
|dla ilu osób nieprzydatna|span\[id^="votes-no"\]|useless||
|data wystawienia opinii|span.user-post__publlished > time:nth-child(1)["datetime"]|publish_date||
|data zakupu|span.user-post__publlished > time:nth-child(2)["datetime"]|purchase_date||