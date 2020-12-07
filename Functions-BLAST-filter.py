#this file must be inside TBLASTn-resulsts directory to locate 
import re
import xlsxwriter

#create a workbook and a worksheet ---> ('newfilename.xlsx')
workbook = xlsxwriter.Workbook('zeta-carotene-desaturase.xlsx')
worksheet = workbook.add_worksheet()

parameters = ('Query Name', 'Query Acss Number', 'Contig Acss Number', 'Score (Bits)', 'Expect', 'Frame', 'Start', 'Stop')

row = 0
col = 0
data_id_row = 0

#creating .xlsx headers
for item in parameters:
    worksheet.write(row, col, item)
    col +=1
#set file path 
filename = "/home/barrel/Desktop/Biologia/P5/Bioinformática/Projeto_Bioinfo/BLAST-DATA/CTP4/BLAST-results/TBLASTN-results/blast-ZDS-zeta-carotene-desaturase-Chlorophyta.txt"
fi = open(filename, "r")

contents = fi.readlines()

#function to create a list with query id
def query_id(string_line): 
    #(?<=y\s) means lookahead regex match and do not count y=\s in match result
    q_id = re.search(r"(?<=y=\s)...+", string_line) 
    str_qid = q_id.group()

    #create a list = [query acess number, query name]
    sep_id = re.split(r"(?<=\.\d)", str_qid) 
    return sep_id

#function to find contig_id in each line
def contig_id(string_line):
    contig_id = re.search(r"^>\w+", string_line, re.MULTILINE)
    return contig_id.group()

#function to store contig data (score) for each alingment
def score_data(string_line):
    score_data = re.search(r"\bScore\b\s\=\s\d+.\d", string_line)
    return score_data.group()


#function to store contig data (expect) for each alingment 
def expect_value(string_line): 
    #regex \bExpect matches exactly tihs characters after \b(bounderies), + is greedy search. (?=,) is look behind match ','.
    expect_data = re.search(r"\bExpect...+(?=,)", string_line)
    return expect_data.group()

#function to store contig data (frame) for each alingment
def frame_data(string_line):
    frame_data = re.search(r"\bFrame\s=\s.+", string_line)
    
    return frame_data.group()


    

#iterating over blastresults data for each line
for line in contents:
    #caso encontre query data, escrevê-lo em  worksheet
    if re.search(r"(?<=y=\s)...+", line) != None:
        #data_id_row += 1
        row += 2
    #atualizar query_data para preenchimento da célula (novo query)
        query_data = query_id(line)
        worksheet.write(row, 0, query_data[1])
        worksheet.write(row, 1, query_data[0])
        
    #caso encontre contig id em line
    elif re.search(r"^>\w+", line) != None: 
        #data_id_row += 1    
        row += 1
        contig_str_id = contig_id(line)
        worksheet.write_string(row, 2, contig_str_id)
    #a cada iteração do 'for', preencher células abaixo do primeiro match do id,
    #enquanto este id não for atualizado

    
    #caso encontre score data em line
    if re.search(r"\bScore\b\s\=\s\d+.\d", line):
        score_str_data = score_data(line)
        worksheet.write_string(row, 3, score_str_data)
    #caso encontre expect value data
    if re.search(r"\bExpect...+(?=,)", line):
        e_value_data = expect_value(line)
        worksheet.write_string(row, 4, e_value_data)
    #caso encontre frame value
    if re.search(r"\bFrame\s=\s.+", line):
        frame_str_data = frame_data(line)
        worksheet.write_string(row, 5, frame_str_data)
        #testing jumping lines inside last function called (provisório ser em frame, final version sera em 'stop')
        row +=1

    


        
    

    










fi.close()
workbook.close()
