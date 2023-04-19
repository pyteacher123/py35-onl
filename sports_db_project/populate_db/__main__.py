import sys
from data_access import SqliteGateway
from data_access.dao import (
    CountryDAO,
    ProducerDAO,
    SneakerDAO,
    SportDAO,
    TeamDAO
)
from fake_lib.providers import (
    CountryProvider,
    RandomValueFromListProvider,
    TextProvider,
    SportwareCompanyProvider,
    ColorProvider,
    PriceProvider,
    WordProvider,
    SportProvider,
    IsTeamProvider
)
from factories import (
    CountryFactory,
    ProducerFactory,
    SneakerFactory,
    SportFactory,
    TeamFactory
)
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

    producers_list = producer_dao.get_ids_list()
    sneaker_dao = SneakerDAO(db_gateway=db_gateway)
    sneaker_factory = SneakerFactory(
        word_provider=WordProvider(),
        price_provider=PriceProvider(),
        random_value_provider=RandomValueFromListProvider(producers_list),
        color_provider=ColorProvider()
    )
    PopulateTable(
        records_number=records_number,
        dao=sneaker_dao,
        fake_factory=sneaker_factory
    ).execute()

    sport_dao = SportDAO(db_gateway=db_gateway)
    sport_factory = SportFactory(
        sport_provider=SportProvider(),
        is_team_provider=IsTeamProvider()
    )
    PopulateTable(
        records_number=records_number,
        dao=sport_dao,
        fake_factory=sport_factory
    ).execute()

    sports_lists = sport_dao.get_ids_list()
    team_dao = TeamDAO(db_gateway=db_gateway)
    team_factory = TeamFactory(
        name_provider=WordProvider(),
        country_id_provider=RandomValueFromListProvider(countries_list),
        description_provider=TextProvider(),
        sport_type_id_provider=RandomValueFromListProvider(sports_lists)
    )
    PopulateTable(
        records_number=records_number,
        dao=team_dao,
        fake_factory=team_factory
    ).execute()
