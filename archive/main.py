import LoadStructure
import VariantGenerator
from TaskGenerator import TaskGenerator


# TODO Кажется этот файл можно удалить

if __name__ == '__main__':
    LoadStructure.generate_stracture()
    VariantGenerator.GenerateVariantsDistributionOld(random_seed_parametr=0)
    first_task = TaskGenerator()
    first_task.create_task()

