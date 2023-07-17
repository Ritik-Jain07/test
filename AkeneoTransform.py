AkeneoTransform.py
import json


class Transform:
    def __init__(self):
        pass

    def parse_attributes(self, product_model):
        grouped_attributes = {}
        for attribute in product_model:
            attribute_group = f"{attribute.split('_')[0]}_attributes"
            if attribute_group not in grouped_attributes.keys():
                # print('attribute group is new')
                grouped_attributes[attribute_group] = {}
            attributes_data = []
            if len(product_model[attribute]) > 1:
                print(f'More than one attribute {attribute}')
                for data in product_model[attribute]:
                    attributes_data.append(data['data'])
                grouped_attributes[attribute_group][attribute] = attributes_data
            else:
                grouped_attributes[attribute_group][attribute] = product_model[attribute][0]['data']
        return grouped_attributes

    def transform_product_models(self, data):
        processed = []
        print(f'Transforming {len(data)} product models')
        for product_model in data:
            product_model = json.loads(product_model)
            product_model_transformed = {'code': product_model['code'],
                                         'family': product_model['family'],
                                         'family_variant': product_model['family_variant'],
                                         'parent': product_model['parent'],
                                         'categories': product_model['categories'],
                                         'created_at': product_model['created'],
                                         'updated_at': product_model['updated'],
                                         'metadata': product_model['metadata']
                                         }
            parsed_attributes = self.parse_attributes(product_model['values'])
            for grouped_attributes in parsed_attributes:
                product_model_transformed[grouped_attributes] = parsed_attributes[grouped_attributes]

            processed.append(json.dumps(product_model_transformed))
        return processed

    def transform_products(self, data):
        processed = []
        print(f'Transforming {len(data)} products')
        for product in data:
            product = json.loads(product)
            # print(product)
            products_transformed = {'identifier': product['identifier'],
                                    'enabled': product['enabled'],
                                    'family': product['family'],
                                    'parent': product['parent'],
                                    'categories': product['categories'],
                                    'created_at': product['created'],
                                    'updated_at': product['updated'],
                                    'metadata': product['metadata']
                                    }
            parsed_attributes = self.parse_attributes(product['values'])
            for grouped_attributes in parsed_attributes:
                products_transformed[grouped_attributes] = parsed_attributes[grouped_attributes]

            processed.append(json.dumps(products_transformed))
        return processed