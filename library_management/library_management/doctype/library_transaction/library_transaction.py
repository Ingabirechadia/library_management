# Copyright (c) 2026, Chadia and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibraryTransaction(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from library_management.library_management.doctype.library_transaction_item.library_transaction_item import (
			LibraryTransactionItem,
		)

		amended_from: DF.Link | None
		due_date: DF.Date | None
		issue_reference: DF.Link | None
		items: DF.Table[LibraryTransactionItem]
		member: DF.Link
		posting_date: DF.Date | None
		total_fine: DF.Currency
		transaction_type: DF.Literal["Issue,Return"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Library Transaction"
