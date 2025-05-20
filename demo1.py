print(
All·student·Details:⏎	
·[[301.··67.··77.··88.]⏎	
·[302.··78.··88.··77.]⏎	
·[303.··45.··56.··89.]⏎	
·[304.··88.··98.··45.]⏎	
·[305.··78.··88.··99.]⏎	
·[306.··68.··78.··36.]⏎	
·[307.··79.··12.··45.]⏎	
·[308.··46.··45.··77.]⏎	
·[309.··89.··32.··88.]⏎	
·[310.··79.··24.··33.]]⏎	
Total·Students:·10⏎	
All·Student·Roll·Nos·[301.·302.·303.·304.·305.·306.·307.·308.·309.·310.]⏎	
Subject·1·Marks·[67.·78.·45.·88.·78.·68.·79.·46.·89.·79.]⏎	
Min·marks·in·Subject·2·12.0⏎	
Max·marks·in·Subject·3·99.0⏎	
All·subject·marks:·[[67.·77.·88.]⏎	
·[78.·88.·77.]⏎	
·[45.·56.·89.]⏎	
·[88.·98.·45.]⏎	
·[78.·88.·99.]⏎	
·[68.·78.·36.]⏎	
·[79.·12.·45.]⏎	
·[46.·45.·77.]⏎	
·[89.·32.·88.]⏎	
·[79.·24.·33.]]⏎	
Total·Marks·[232.·243.·190.·231.·265.·182.·136.·168.·209.·136.]⏎	
[77.3·81.··63.3·77.··88.3·60.7·45.3·56.··69.7·45.3]⏎	
Average·Marks·of·each·subject·[71.7·59.8·67.7]⏎	
Average·Marks·of·S1·and·S2·[71.7·59.8]⏎	
Average·Marks·of·S1·and·S3·[71.7·67.7]⏎	
Roll·no·who·got·maximum·marks·in·Subject·3·305.0⏎	
Roll·no·who·got·minimum·marks·in·Subject·2·307.0⏎	
Roll·no·who·got·24·marks·in·Subject·2·[[310.]]⏎	
Count·of·students·who·got·marks·in·Subject·1·<·40·0⏎	
Count·of·students·who·got·marks·in·Subject·2·>·90:·1⏎	
Count·of·students·in·each·subject·who·got·marks·>=·90:·[0·1·1]⏎	
Roll·no:·[301.·302.·303.·304.·305.·306.·307.·308.·309.·310.]⏎	
Count·of·subjects·in·which·student·got·marks·>=·90:·[0·0·0·1·1·0·0·0·0·0]⏎	
[45.·46.·67.·68.·78.·78.·79.·79.·88.·89.]⏎	
[[301.··67.··77.··88.]⏎	
·[302.··78.··88.··77.]⏎	
·[304.··88.··98.··45.]⏎	
·[305.··78.··88.··99.]⏎	
·[306.··68.··78.··36.]⏎	
·[307.··79.··12.··45.]⏎	
·[309.··89.··32.··88.]⏎	
·[310.··79.··24.··33.]]⏎	
[[301.··67.··77.··88.]⏎	
·[302.··78.··88.··77.]⏎	
·[303.··45.··56.··89.]⏎	
·[304.··88.··98.··45.]⏎	
·[305.··78.··88.··99.]⏎	
·[306.··68.··78.··36.]⏎	
·[307.··79.··12.··45.]⏎	
·[308.··46.··45.··77.]⏎	
·[309.··89.··32.··88.]⏎	
·[310.··79.··24.··33.]]⏎	
(array([6,·9],·dtype=int32),)⏎	

OperationsOnStudentData.py
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
print("Total Marks",np.sum(allsub,axis=1))

# 9. print average marks of each student
print(np.mean(allsub,axis=1))
averagemarksstd=np.round(np.mean(allsub,axis=1),1)
# 10. print average marks of each subject
averagemarkssub=np.mean(allsub,axis=0)
print("Average Marks of each subject", averagemarkssub)

# 11. print average marks of S1 and S2
print("Average Marks of S1 and S2", averagemarkssub[:2] )

# 12. print average marks of S1 and S3
print("Average Marks of S1 and S3", averagemarkssub[[0,2]] )

# 13. print Roll number who got maximum marks in Subject 3
maxsub3ind=np.argmax(sub3)
print("Roll no who got maximum marks in Subject 3", roll_nos[maxsub3ind] )

# 14. print Roll number who got minimum marks in Subject 2
minsub2ind=np.argmin(sub2)
print("Roll no who got minimum marks in Subject 2", roll_nos[minsub2ind] )

# 15. print Roll number who got 24 marks in Subject 2
rollwith24=roll_nos[sub2==24]
print("Roll no who got 24 marks in Subject 2", rollwith24.reshape(-1,1) )

# 16. print count of students who got marks in Subject 1 < 40

print("Count of students who got marks in Subject 1 < 40", np.sum(sub1<40) )

# 17. print count of students who got marks in Subject 2 > 90
print("Count of students who got marks in Subject 2 > 90:", np.sum(sub2>90) )

# 18. print count of students in each subject who got marks >= 90
count90psub = np.sum(allsub >= 90,axis=0)
print("Count of students in each subject who got marks >= 90:", count90psub )

# 19. print count of subjects in which each student got marks >= 90
count90pstd = np.sum(allsub >= 90 ,axis = 1)
print("Roll no:",roll_nos)
print("Count of subjects in which student got marks >= 90:", count90pstd )

# 20. Print S1 marks in ascending order
print(np.sort(sub1))

# 21. Print S1 marks >= 50 and <= 90

mask5090 = (sub1 >= 50)& (sub1 <= 90)
print(a[mask5090])
# 22. Print the index position of marks 79
print(a)
indices79 = np.where(sub1 == 79)
print(indices79)


"""
print()
Reason for late submission
Eucs.Learner.Contents.LateSubmissionModal.Input.Placeholder
Please enter at least 15 characters

)