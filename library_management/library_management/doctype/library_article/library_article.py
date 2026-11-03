# Copyright (c) 2026, Chadia and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibraryArticle(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		author: DF.Data | None
		available_copies: DF.Int
		category: DF.Literal["fiction,Science,History,Refetrence,Other"]
		isbn: DF.Data | None
		shelf_location: DF.Data | None
		title: DF.Data
		total_copies: DF.Int
	# end: auto-generated types

	_DOCTYPE_NAME = "Library Article"
