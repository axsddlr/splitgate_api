import re

from utils.utils import get_soup, get_status, get_requests


class Splitgate:
    @staticmethod
    def get_news():
        URL = f"https://www.splitgate.com/splitgate-news"
        status = get_status(URL)
        response = get_soup(URL)

        base = response.find("div", {"class": re.compile("collection-list-2 w-dyn-items")})
        container = base.find_all("div", {"class": re.compile("div-block-127")})

        links = []
        for containers in container:
            url = containers.find("a")["href"]
            links.append("https://www.splitgate.com/" + url)

            api = []
            for link in links:
                r = get_soup(link)

                # get title
                title = r.find("h1", {"class": "blog-title big"}).text
                # get date
                date = r.find("p", {"class": "paragraph-19 date"}).text

                # get content from the article
                contents = []
                for content in r.find_all("p"):
                    contents.append(content.text)

                # get image from the article
                try:
                    imgs = []
                    for img in r.find_all("img"):
                        imgs.append(img["src"])
                except:
                    imgs = None

                api.append(
                    {
                        "title": title,
                        "summary": contents[1] + " " + contents[3],
                        "thumbnail": imgs[1],
                        "date": date,
                    }
                )

        data = {"status": status, "data": api}

        return data

    # @staticmethod
    # def proseries_news():
    #     URL = "https://splitgateproseries.com/api/articles"
    #     status = get_status(URL)
    #     apiResponse = get_requests(URL)
    #     links = []
    #     for each in apiResponse:
    #         slug = "https://splitgateproseries.com/api/article?slug=" + each["slug"]
    #         links.append(slug)
    #
    #     # la_base = response.find("div", {"class": re.compile("collection-list-2 w-dyn-items")})
    #     # la_module = la_base.find_all("div", {"class": re.compile("div-block-127")})
    #     #
    #     # links = []
    #     # for module in la_module:
    #     #     url = module.find("a")["href"]
    #     #     links.append("https://www.splitgate.com/" + url)
    #     #
    #         api = []
    #         for link in links:
    #             r = get_requests(link)
    #             # get title
    #             title = r["title"]
    #
    #             # get title
    #             # title = r.find("h2")
    #     #         # get date
    #     #         date = r.find("p", {"class": "paragraph-19 date"}).text
    #     #
    #     #         # get content from the article
    #     #         contents = []
    #     #         for content in r.find_all("p"):
    #     #             contents.append(content.text)
    #     #
    #     #         # get image from the article
    #     #         try:
    #     #             imgs = []
    #     #             for img in r.find_all("img"):
    #     #                 imgs.append(img["src"])
    #     #         except:
    #     #             imgs = None
    #     #
    #     #         api.append(
    #     #             {
    #     #                 "title": title,
    #     #                 "summary": contents[1] + " " + contents[3],
    #     #                 "thumbnail": imgs[1],
    #     #                 "date": date,
    #     #             }
    #     #         )
    #     #
    #     # data = {"status": status, "data": api}
    #
    #     return title


if __name__ == '__main__':
    print(Splitgate.news())
