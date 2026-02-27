# import re
# import sys
#
# def checkFormatStr(s:str) -> bool:
#     """
#     Проверяет строку.
#     """
#     pattern = r'^[ACGT]*$'   # * - любые вариации
#     return bool(re.match(pattern, s))
# 
#
# def compress(gene) -> int:
#     """
#     Сжимает строку нуклеотидов
#     """
#     if not  checkFormatStr(gene):
#         return 0
#     bitString =1
#     for nucleotide in gene:
#         bitString<<=2
#         if nucleotide=='A':
#             bitString |= 0b00
#         elif nucleotide=='C':
#             bitString |= 0b01
#         elif nucleotide=='G':
#             bitString |= 0b10
#         elif nucleotide=='T':
#             bitString |= 0b11
#         else:
#             return 0
#     return bitString
#
# def decompress(bitString) -> int:
#     """
#     Расшифровываем строку нуклеотидов
#     """
#
#     gene = []
#     while bitString > 1:
#         bits = bitString & 0b11
#         if bits == 0b00:
#             gene.append('A')
#         elif bits == 0b01:
#             gene.append('C')
#         elif bits == 0b10:
#             gene.append('G')
#         elif bits == 0b11:
#             gene.append('T')
#         bitString >>= 2
#     return gene[::-1]
#
#
#
#
#
# gene = 'TAGGGATTAAC'
# bit_string = compress(gene)
# print ( bit_string) # 7513025
# print ( decompress(compress(gene)) )
# print("Size gene: ", sys.getsizeof(gene))
# print("Size geneNew: ", sys.getsizeof(bit_string))
