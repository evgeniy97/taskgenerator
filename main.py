import VariantGenerator
import InsertVariant

if __name__ == '__main__':
    VariantGenerator.variantgenerator(seed=0).GenerateVariantsDistribution()
    InsertVariant.VariantGenerator(BDPath='BaseNotebooks.LR2DB').insert_tasks()



