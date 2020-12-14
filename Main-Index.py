""" Recieve And Process """
import faculty as fac

def main():
    """ Recieve A Score """
    pat = dict()
    score = {
        "GAT": float(input("GAT: ")),
        "GAT TH": float(input("GAT1: ")),
        "GAT ENG": float(input("GAT2: ")),
    }
    for i in range(7):
        pat.update( {"PAT%s" % str(i +1) : float(input("PAT%s: " % str(i +1)))})
    score.update(pat)

    faculty_branch = dict()
    for i in range(5):
        faculty_branch.update({"Order %d" %(i + 1): input("คณะและสาขา: ").strip().split(" ")})

    faculty_score = []

    for order in faculty_branch:
        if faculty_branch[order][0] == "คณะวิศวกรรมศาสตร์":
            result = fac.engineering(score["GAT"], score["PAT1"], score["PAT3"])
        elif faculty_branch[order][0] == "คณะวิศวกรรมศาสตร์(หลักสูตรนานาชาติ)":
            result = fac.engineering_national(score["GAT TH"], score["GAT ENG"], score["PAT1"], score["PAT3"])
        elif faculty_branch[order][0] == "คณะวิทยาศาสตร์":
            result = fac.science(score["GAT"], score["PAT1"], score["PAT2"], faculty_branch[order][1])
        elif faculty_branch[order][0] == "คณะสถาปัตยกรรมศาสตร์":
            result = fac.architecture(score["GAT"], score["PAT4"], score["PAT6"], faculty_branch[order][1])
        elif faculty_branch[order][0] == "คณะบริหารธุรกิจ":
            result = fac.business_administration(score["GAT"], score["PAT1"])
        elif faculty_branch[order][0] == "คณะเทคโนโลยีสารสนเทศ":
            result = fac.information_technology(score["GAT"], score["PAT1"])
        elif faculty_branch[order][0] == "คณะอุตสาหกรรมอาหาร":
            result = fac.food_industry(score["GAT"], score["PAT1"], score["PAT2"], faculty_branch[order][1])
        elif faculty_branch[order][0] == "คณะครุศาสตร์อุตสาหกรรมและเทคโนโลยี":
            result = fac.education_industry_technology(score["GAT"], score["PAT2"], score["PAT3"], score["PAT4"], score["PAT5"], faculty_branch[order][1])
        elif faculty_branch[order][0] == "คณะเทคโนโลยีการเกษตร":
            result = fac.agricultural_technology(score["GAT TH"], score["PAT1"], score["PAT2"])
        elif faculty_branch[order][0] == "วิทยาลัยนวัตกรรมการผลิตขั้นสูง":
            result = fac.engineering_manufacturing(score["PAT1"], score["PAT2"], score["PAT3"])
        elif faculty_branch[order][0] == "วิทยาลัยนาโนเทคโนโลยีพระจอมเกล้าลาดกระบัง":
            result = fac.bachelor_technokmitl(score["GAT"], score["PAT1"], score["PAT2"])
        elif faculty_branch[order][0] == "วิทยาลัยอุตสาหกรรมการบินนานาชาติ":
            result = fac.aviation_industry(score["GAT"], score["PAT1"], score["PAT3"], faculty_branch[order][1])
        elif faculty_branch[order][0] == "วิทยาลัยวิศวกรรมสังคีต":
            result = fac.imse(score["GAT"], score["PAT1"], score["PAT3"])
        elif faculty_branch[order][0] == "วิทยาเขตชุมพรเขตรอุดมศักดิ์ จังหวัดชุมพร":
            result = fac.kmitl_pcc(score["GAT"], score["PAT1"], score["PAT2"], score["PAT3"], faculty_branch[order][0])
        else:
            ## ถ้ากรอกผิดต้องกรอกใหม่
            print("Error")
            main()

        faculty_score.append([result, faculty_branch[order][0]])


    for j in faculty_score:
        print(j[1], "%.2f" % float(j[0]))


main()
