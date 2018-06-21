import LoadStructure,VariantGenerator,TaskGenerator

if __name__ == '__main__':
    LoadStructure.generate_stracture()
    VariantGenerator.GenerateVariantsDistribution(random_seed_parametr=0)
    TaskGenerator.CreateTask()
