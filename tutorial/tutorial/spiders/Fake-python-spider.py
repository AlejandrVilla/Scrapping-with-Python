import scrapy

class FakePythonSpider(scrapy.Spider):
    name = "jobs"
    start_urls=[
        "https://realpython.github.io/fake-jobs/",
    ]

    def parse(self, response):
        for job_link in response.css("a.card-footer-item::attr(href)"):
            if job_link:
                # Seguir el enlace
                yield response.follow(job_link, callback=self.parse_job)

    def parse_job(self, response):
        job = response.css("div.box")
        yield{
            "job": job.css("h1.title::text").get(),
            "company": job.css("h2.subtitle::text").get(),
            # "Location": job.css("p.location::text").get().strip().replace('\n', ''),
            "location": job.css("#location::text").get().strip(),
        }