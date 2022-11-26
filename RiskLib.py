# .........................................................................
# ............................RISKLIB......................................
# .........................................................................

# Library that provides different functions for risk calculation
# Author: Igor Bernardes Urias (2022)

# Function that calculates the forward value of an interest rate
def forward_rate(ra, rb, ta, tb):
    '''
    Function that performs the calculation of a forward rate in a scalar way
    Args:
    =====
    ra (float): Initial interest rate. Conrresponds to the first interpolation vertex (spot rate at ta)
    rb (float): Final interest rate. Corresponds to the second interpolation vertex (spot rate at tb)
    ta (float): First period. Conrresponds to the first interpolation vertex (ta)
    tb (float): End period. Corresponds to the second interpolation vertex (tb)
    Returns:
    ========
    f (float): forward rate
    '''

    # Forward Calculation
    f = ((1.0 + rb)**tb)/((1.0 + ra)**ta) - 1

    return f


# Function that calculates the forward value of interest rate given a list of maturity dates
# and a list of spot rates
def calc_forward_rate(dates, spotRates):
    '''
    Function that receives a maturity date vector and a spot rate vector and calculates the forward
    Args:
    =====
    dates (numpy.array):
    spotRates (numpy.array):
    Returns:
    ========
    fowards (numpy.array): calculated forward values
    '''
    try:

        # array of calculated forwards
        fs = []

        # Check if the lists are compatible to calculate de forward values
        if (len(dates) > 0 and len(spotRates) > 0) and (len(dates) == len(spotRates)):

            totalVertex = len(dates)

            for i in range(totalVertex):

                if i < (totalVertex - 1):
                    
                    ta = dates[i]
                    tb = dates[i + 1]
                    
                    ra = spotRates[i]
                    rb = spotRates[i + 1]

                    f = forward_rate(ra, rb, ta, tb)

                    fs.append([tb,f])

            # Return the structure that contains the calculated forwards
            return fs
    
        else:
            # Parameters incompatibles to calculate the forwards
            return None
    
    except ValueError:
        # Returns a exception
        return ValueError


# Function responsible for calculating the value of the balanced forward price based on domestic 
# and international rates and spot rate.
def calc_pte(rc, rd, ri, t, b):
    '''
    Calculate the value of the balanced forward price
    Args:
    =====
    rc (numpy.array): spot exchange rate
    rd (numpy.array): domestic interest rate
    ri (numpy.array): international interest rate
    t (float): time interval
    b (float): calculation convention (basis)
    Returns:
    ========
    pte (numpy.array): balanced forward price
    '''
    try:
        pte = rc * ( 1.0 + rd)**(t/b)/(1.0 + ri * (t/b))
        return pte
    except:
        return None

