# Copyright 2019 AstroLab Software
# Author: Julien Peloton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pyspark.sql.functions import pandas_udf, PandasUDFType
from pyspark.sql.types import DoubleType, StringType

import pandas as pd
import numpy as np

import requests

import os

from fink_science.tester import spark_unit_tests

# TODO: use logging

@pandas_udf(StringType(), PandasUDFType.SCALAR)
def transoda(
        oid, jd, ra, dec
        ) -> pd.Series:
    """ 
        help will go here
    """
    # Compute the test_features: fit_all_bands

    print("jd:", jd)

    out=[]

    # request many times!
    for i,j in jd.iteritems():
        print("i, one jd:", i, j)

        url = "https://www.astro.unige.ch/cdci/astrooda/dispatch-data/gw/timesystem/api/v1.0/converttime/IJD/{}/REVNUM".format(j-2451544.5)
        print("url:", url)

        try:
            r = requests.get(url)
        except Exception as e:
            print("undefined exception:", e)
            out.append("fail")
        else:
            if r.status_code == 200:
                print("got", r.text)
                out.append(r.text)
            else:
                print("got failure", r.text)
                out.append("fail")

    return pd.Series(out)


if __name__ == "__main__":
    """ Execute the test suite """

    globs = globals()
    ztf_alert_sample = 'fink_science/data/alerts/alerts.parquet'
    globs["ztf_alert_sample"] = ztf_alert_sample

    # Run the test suite
    spark_unit_tests(globs)
