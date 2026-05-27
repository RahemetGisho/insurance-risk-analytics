from scipy.stats import ttest_ind, chi2_contingency


def run_ttest(group_a, group_b):
    """
    Run independent t-test.
    """

    stat, p = ttest_ind(
        group_a,
        group_b,
        equal_var=False
    )

    return {
        "t_statistic": stat,
        "p_value": p
    }


def run_chi_square(contingency_table):
    """
    Run chi-square test.
    """

    chi2, p, dof, expected = chi2_contingency(
        contingency_table
    )

    return {
        "chi2_statistic": chi2,
        "p_value": p
    }
