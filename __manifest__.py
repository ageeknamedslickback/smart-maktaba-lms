# -*- coding: utf-8 -*-

{
    "name": "Smart Maktaba",
    "version": "1.0",  # find a way to make this dynamic
    "depends": ["base"],
    "summary": "A smart library management system.",
    "description": """
        A library management system is software built to handle the primary housekeeping 
        functions of a library. The purpose of a library management system is to operate 
        a library with efficiency and at reduced costs. Library activities include 
        purchasing books, cataloguing, indexing books, recording books in circulation and 
        stock checking, which when done by automated software eliminates the need for 
        repetitive manual work and minimizes the chances of errors.

        Smart Maktaba LMS is such a system.
    """,
    "data": [
        "security/ir.model.access.csv",
        "views/books.xml",
        "views/book_items.xml",
        "views/libraries.xml",
        "views/members.xml",
        "views/reservations.xml",
        "views/menu.xml",
    ],
}
