def konvert_ke_menit(minggu):
    def konvert_ke_menit_hari(hari):
        def konvert_ke_menit_jam(jam):
            def konvert_ke_menit_menit(menit):
                return minggu * 7 * 24 * 60 + hari * 24 * 60 + jam * 60 + menit

            return konvert_ke_menit_menit

        return konvert_ke_menit_jam

    return konvert_ke_menit_hari


data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit",
]

OutputData = []

for item in data:
    bagian = item.split()
    minggu = int(bagian[0])
    hari = int(bagian[2])
    jam = int(bagian[4])
    menit = int(bagian[6])

    konvert = konvert_ke_menit(minggu)(hari)(jam)(menit)
    OutputData.append(konvert)

print(OutputData)
