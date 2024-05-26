from docxtpl import DocxTemplate
doc = DocxTemplate("invoice_template.docx")


invoice_list = [[2, "pen", 0.5, 1,8],
                [1, "paper pack", 5, 5,8],
                [2, "notebook", 2, 4,8],
                [2, "notebook", 5, 4,8]]

doc.render({"name":"shibin",
            "address":"ayaappally house",
            "phone":"123",
            "email":"shibinsbn.786@gmail.com",
            "invoice_list": invoice_list,
            "total":"100"})
doc.save("new_invoice.docx")