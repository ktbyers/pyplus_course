from pathlib import Path
import pytest
from helpers import subprocess_runner

TEST_CASES = [
    #    COLLATERAL
    "../class7/collateral/test1_jsonrpc.py",
    "../class7/collateral/jrpc_methods.py",
    "../class7/collateral/test1_xml.py",
    "../class7/collateral/xml_methods.py",
    # Exercises
    "../class7/exercises/ex1_xml_basics.py",
    "../class7/exercises/ex2_xmltodict.py",
    "../class7/exercises/ex3_xmltodict_forcelist.py",
    "../class7/exercises/ex4_xml_find.py",
    "../class7/exercises/ex5_xml_namespaces.py",
    "../class7/exercises/ex6_nxapi_jrpc.py",
    "../class7/exercises/ex7_nxapi_xml.py",
]


@pytest.mark.parametrize("test_case", TEST_CASES)
def test_runner(test_case):
    path_obj = Path(test_case)
    python_script = path_obj.name
    script_dir = path_obj.parents[0]
    cmd_list = ["python", python_script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, script_dir)
    assert return_code == 0
    assert std_err == ""
