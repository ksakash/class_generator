from jinja2 import Template

def generate_code(class_name, class_file_name, template_file_name):
    f = open(template_file_name, 'r')
    template = f.read()
    code_template = Template(template)
    code = code_template.render({"class_name": class_name})
    f.close()
    f = open(class_file_name, 'w+')
    print(code)
    f.write(code)
    f.close()

def create_class(crawler_type, class_filename, class_name):
    crawler_template_map = {
        "product": "product_crawler.py.jinja2",
        "review": "review_crawler.py.jinja2",
        "search": "search_crawler.py.jinja2"
    }
    template_file_name = crawler_template_map[crawler_type]
    generate_code(class_name, class_filename, template_file_name)


if __name__ == "__main__":
    class_name = "AmazonReviewCrawler"
    class_file_name = "amazon_review_crawler.py"
    crawler_type = "review"
    create_class(crawler_type, class_file_name, class_name)
