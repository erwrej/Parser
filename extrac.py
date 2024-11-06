# -*- coding: utf-8 -*-

import re
import logging

# Function to get Артикул Маркета
def get_market_article(tree):
    try:
        return tree.xpath('//span[contains(@class, "WWV1V") and contains(@class, "_2sMuA6") and contains(@class, "_3kBfF") and contains(@class, "_1ASyY")]/text()')[0].strip()
    except IndexError:
        logging.warning("Артикул не найден.")
        return None

# Function to get Бренд
def get_brand(tree):
    try:
        return tree.xpath('//a[contains(@class, "product-page__header-brand")]/text()')[0].strip()
    except IndexError:
        logging.warning("Бренд не найден.")
        return None

# Function to get Линейка
def get_series(tree):
    try:
        return tree.xpath('//td[contains(text(), "Линейка")]/following-sibling::td/span/text()')[0].strip()
    except IndexError:
        logging.warning("Линейка не найдена.")
        return None

# Function to get Процессор
def get_processor(tree):
    try:
        return tree.xpath('//td[contains(text(), "Процессор")]/following-sibling::td/span/text()')[0].strip()
    except IndexError:
        logging.warning("Процессор не найден.")
        return None

# Function to get Разрешение экрана
def get_screen_resolution(tree):
    try:
        return tree.xpath('//td[contains(text(), "Разрешение экрана")]/following-sibling::td/span/text()')[0].strip()
    except IndexError:
        logging.warning("Разрешение экрана не найдено.")
        return None

# Function to get Вес
def get_weight(tree):
    try:
        return tree.xpath('//td[contains(text(), "Вес")]/following-sibling::td/span/text()')[0].strip()
    except IndexError:
        logging.warning("Вес не найден.")
        return None

# Function to get Время автономной работы
def get_battery_life(tree):
    try:
        return tree.xpath('//td[contains(text(), "Время автономной работы")]/following-sibling::td/span/text()')[0].strip()
    except IndexError:
        logging.warning("Время автономной работы не найдено.")
        return None

# Function to get Тип матрицы экрана
def get_screen_matrix_type(tree):
    try:
        return tree.xpath('//td[contains(text(), "Тип матрицы экрана")]/following-sibling::td/span/text()')[0].strip()
    except IndexError:
        logging.warning("Тип матрицы экрана не найден.")
        return None

# Function to get Тип покрытия экрана
def get_screen_coating_type(tree):
    try:
        return tree.xpath('//td[contains(text(), "Тип покрытия экрана")]/following-sibling::td/span/text()')[0].strip()
    except IndexError:
        logging.warning("Тип покрытия экрана не найден.")
        return None

# Function to get Диагональ экрана
def get_screen_diagonal(tree):
    try:
        return tree.xpath('//td[contains(text(), "Диагональ экрана")]/following-sibling::td/span/text()')[0].strip()
    except IndexError:
        logging.warning("Диагональ экрана не найдена.")
        return None

# Function to get Оперативная память
def get_ram(tree):
    try:
        return tree.xpath('//td[contains(text(), "Оперативная память")]/following-sibling::td/span/text()')[0].strip()
    except IndexError:
        logging.warning("Оперативная память не найдена.")
        return None

# Function to get Объем видеопамяти
def get_video_memory(tree):
    try:
        return tree.xpath('//td[contains(text(), "Объем видеопамяти")]/following-sibling::td/span/text()')[0].strip()
    except IndexError:
        logging.warning("Объем видеопамяти не найден.")
        return None

# Function to get Гарантийный срок
def get_warranty_period(tree):
    try:
        return tree.xpath('//td[contains(text(), "Гарантийный срок")]/following-sibling::td/span/text()')[0].strip()
    except IndexError:
        logging.warning("Гарантийный срок не найден.")
        return None

# Function to get Операционная система
def get_operating_system(tree):
    try:
        return tree.xpath('//td[contains(text(), "Операционная система")]/following-sibling::td/span/text()')[0].strip()
    except IndexError:
        logging.warning("Операционная система не найдена.")
        return None

