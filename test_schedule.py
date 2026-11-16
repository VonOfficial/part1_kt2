import pytest
import allure
import schedule as schedule_module


@pytest.fixture
def schedule():
    return schedule_module.SCHEDULE


@allure.epic("Практическая работа 2")
@allure.feature("Расписание занятий")
@allure.story("Количество часов за день")
@allure.severity(allure.severity_level.NORMAL)
class TestHoursInDay:

    @allure.title("Количество часов за {day}")
    @pytest.mark.parametrize(
        "day, expected",
        [
            ("понедельник", 5.5),
            ("вторник", 4),
            ("среда", 2),
            ("четверг", 3),
            ("пятница", 4),
            ("суббота", 2),
            ("воскресенье", 4),
        ],
    )
    def test_hours_in_day(self, schedule, day, expected):
        assert schedule_module.hours_in_day(schedule, day) == expected


@allure.epic("Практическая работа 2")
@allure.feature("Расписание занятий")
@allure.story("Допустимые типы занятий")
@allure.severity(allure.severity_level.CRITICAL)
class TestCorrectTypes:

    @allure.title("Типы занятий за {day}")
    @pytest.mark.parametrize(
        "day, expected",
        [
            ("понедельник", True),
            ("вторник", True),
            ("среда", True),
            ("четверг", True),
            ("пятница", False),

            pytest.param(
                "суббота",
                True,
                marks=pytest.mark.skip(
                    reason="В спецификации не указаны допустимые типы занятий для субботы"
                ),
            ),

            ("воскресенье", False),
        ],
    )
    def test_is_correct_types(self, schedule, day, expected):
        assert schedule_module.is_correct_types(schedule, day) is expected


@allure.epic("Практическая работа 2")
@allure.feature("Расписание занятий")
@allure.story("Список предметов")
@allure.severity(allure.severity_level.NORMAL)
class TestGetSubjects:

    @allure.title("Предметы за {day}")
    @pytest.mark.parametrize(
        "day, expected",
        [
            (
                "понедельник",
                ["Математика", "Программирование", "История"],
            ),
            (
                "вторник",
                ["Физика", "Физика"],
            ),
            (
                "среда",
                ["Базы данных"],
            ),
            (
                "четверг",
                ["Английский язык"],
            ),
            (
                "пятница",
                ["Программирование", "Математика"],
            ),
            (
                "суббота",
                ["Проектная деятельность"],
            ),
            (
                "воскресенье",
                ["День открытых дверей", "Математика"],
            ),
        ],
    )
    def test_get_subjects(self, schedule, day, expected):
        assert schedule_module.get_subjects(schedule, day) == expected
