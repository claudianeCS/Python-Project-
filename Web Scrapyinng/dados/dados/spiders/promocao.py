import scrapy


class PromocaoSpider(scrapy.Spider):
    name = 'promocao'

    start_urls = [f'https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-1&page={i}' for i in range(1, 43)]

    def parse(self, response, **kwargs):
        for topo in response.xpath('//li[@class="promotion-item default"]'):
            descricao = topo.xpath('.//p[@class="promotion-item__title"]//text()').get()
            preço_normal = topo.xpath('.//span[@class="promotion-item__oldprice"]//text()').getall()
            preço_promocao = topo.xpath('.//span[@class="promotion-item__price"]//text()').getall()
            desconto = topo.xpath('.//span[@class="promotion-item__discount"]//text()').getall()

            yield {
                'nome_do_produto': descricao,
                'preco_original': preço_normal,
                'desconto': desconto,
                'preco_disconto': preço_promocao
            }

