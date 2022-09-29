'''
Author: MJ.XU
Date: 2022-08-07 17:29:42
LastEditTime: 2022-08-09 09:16:31
LastEditors: MJ.XU
Description: 
Personal URL: https://www.squirrelled.cn/
'''
# 先考虑5hz的9个点
# Based on https://blog.csdn.net/weixin_43790276/article/details/109191533
import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(0, 10)

plt.figure(figsize=(20, 10), dpi=100)
expected_speed = 1800
game = ['round_00', 'round_01', 'round_02', 'round_03',
        'round_04', 'round_11', 'round_12', 'round_13', 'round_14']
scores = [1816, 1825, 1807, 1816, 1794, 1799, 1775, 1819, 1797]
new_list = [abs(x-expected_speed) for x in scores]
# print(new_list)
# 线的设置
plt.plot(game, scores, c='red', linestyle='--',
         label='Real_speed', markersize=10)  # marker="o"
# 这里可以显示y=1800
# plt.axhline(1800, linestyle='-.', label='Expected_speed')
for i, j in zip(game, scores):
    # https://blog.csdn.net/ukakasu/article/details/81502096?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-81502096-blog-115271218.pc_relevant_multi_platform_featuressortv2removedup&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-81502096-blog-115271218.pc_relevant_multi_platform_featuressortv2removedup&utm_relevant_index=1
    # plt.vlines(i, 1800, j, colors="c", linestyles="dashed")
    # https://blog.csdn.net/TeFuirnever/article/details/88947248
    # https://skylarkprogramming.blog.csdn.net/article/details/124073704?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-124073704-blog-80115300.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-124073704-blog-80115300.pc_relevant_default&utm_relevant_index=1
    plt.text(i, j, '%d' % j, ha='right', va='bottom', fontsize=9)
plt.errorbar(game, scores, yerr=new_list, fmt='o', color='black',
             ecolor='lightgray', elinewidth=3, capsize=0)
# plt.hlines(1825, 'round_00', 'round_01', colors="c", linestyles="dashed")
# plt.plot(x, expected_speed, linestyle='-.')
# 点的设置
# plt.scatter(game, scores, c='blue')
# y轴的量程设置
# https://blog.csdn.net/Poul_henry/article/details/82590392
y_ticks = range(min(scores), max(scores))
plt.yticks(y_ticks[::10])
# https://blog.csdn.net/weixin_39417324/article/details/115271218
# 只使用y轴
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.xlabel("Round quarts", fontdict={'size': 16})
plt.ylabel("Motor speed: *dps", fontdict={'size': 16})
plt.title("Motor speed in 2 rounds with expected speed 1800 dps (5hz)",
          fontdict={'size': 20})
plt.legend(loc="lower right")
plt.show()
# plt.savefig('test.png')
