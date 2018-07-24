import kf_book.gh_internal as gh
import matplotlib.pylab as plt

def plot_hypothesis1():
    #with figsize(y=3.5):
        plt.figure()
        plt.errorbar([1, 2, 3], [170, 161, 169],
                     xerr=0, yerr=10, fmt='bo', capthick=2, capsize=10)

        plt.plot([1, 3], [180, 160], color='g', ls='--')
        plt.plot([1, 3], [170, 170], color='g', ls='--')
        plt.plot([1, 3], [160, 175], color='g', ls='--')
        plt.plot([1, 2, 3], [180, 152, 179], color='g', ls='--')
        plt.xlim(0,4)
        plt.ylim(150, 185)
        plt.xlabel('day')
        plt.ylabel('lbs')
        plt.tight_layout()
        plt.show()


plot_hypothesis1()
