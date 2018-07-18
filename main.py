import VariantGenerator
import ScriptWriter


if __name__ == '__main__':
    VariantGenerator.variantgenerator(seed=0).GenerateVariantsDistribution()
    ScriptWriter.scriptwrite().write()


