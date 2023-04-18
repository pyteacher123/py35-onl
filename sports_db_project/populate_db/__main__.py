import sys
from data_access import SqliteGateway
from data_access.dao import CountryDAO, ProducerDAO
from fake_lib.providers.country import CountryProvider
from fake_lib.providers.random_value import RandomValueFromListProvider
from fake_lib.providers.text import TextProvider
from fake_lib.providers.sport_company import SportwareCompanyProvider
from factories import CountryFactory, ProducerFactory
from populate_table_command import PopulateTable


AVAILABLE_FLAGS = ('-d', '-n')


if __name__ == '__main__':
    config_args = sys.argv[1:]
    for index in range(0, len(config_args), 2):
        flag = config_args[index]
        if flag not in AVAILABLE_FLAGS:
            raise ValueError('Invalid flag.')
        elif flag == '-d':
            db_name = config_args[index + 1]
        elif flag == '-n':
            records_number = int(config_args[index + 1])

    db_gateway = SqliteGateway(db_name=db_name)

    country_dao = CountryDAO(db_gateway=db_gateway)
    country_factory = CountryFactory(country_provider=CountryProvider())
    PopulateTable(
        records_number=records_number,
        dao=country_dao,
        fake_factory=country_factory
    ).execute()

    countries_list = country_dao.get_ids_list()
    producer_dao = ProducerDAO(db_gateway=db_gateway)
    producer_factory = ProducerFactory(
        random_value_provider=RandomValueFromListProvider(countries_list),
        text_provider=TextProvider(),
        sports_company_provider=SportwareCompanyProvider()
    )
    PopulateTable(
        records_number=records_number,
        dao=producer_dao,
        fake_factory=producer_factory
    ).execute()

