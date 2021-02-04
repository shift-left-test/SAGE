import os
import subprocess
import shutil
import pytest
import sys


def test_basic(basic_build):
    proc = subprocess.Popen([
        "sage",
        "--source-path",
        basic_build.src_path,
        "--build-path",
        basic_build.bld_path,
        "--verbose"],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE)

    (output, error) = proc.communicate()

    assert u"cpplint is running..." in str(output), str(output)


def test_basic_with_tool_option(basic_build):
    proc = subprocess.Popen([
        "sage",
        "--source-path",
        basic_build.src_path,
        "--build-path",
        basic_build.bld_path,
        "--verbose",
        "cpplint:--filter=-runtime/indentation_namespace",
        "cppcheck"],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE)

    (output, error) = proc.communicate()

    assert u"cpplint is running..." in str(output)
    assert u"runtime/indentation_namespace" not in str(error)


def test_output(basic_build):
    proc = subprocess.Popen([
        "sage",
        "--source-path",
        basic_build.src_path,
        "--build-path",
        basic_build.bld_path,
        "--output-path",
        "{}/report".format(basic_build.bld_path),
        "--verbose"
        ],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE)
    
    (output, error) = proc.communicate()

    assert os.path.exists("{}/report/sage_report.json".format(basic_build.bld_path))


def test_invalid_tool_path(basic_build):
    proc = subprocess.Popen([
        "sage",
        "--source-path",
        basic_build.src_path,
        "--build-path",
        basic_build.bld_path,
        "--tool-path",
        "/bin",
        "--verbose"],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE)

    (output, error) = proc.communicate()

    assert u"* cpplint is not installed" in str(output)


def test_invalid_build_path(basic_build):
    proc = subprocess.Popen([
        "sage",
        "--source-path",
        basic_build.src_path,
        "--build-path",
        os.path.join(basic_build.bld_path, "tmp"),
        "--verbose"],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE)

    (output, error) = proc.communicate()

    assert u"There is no 'compile_commands.json'" in str(output)


def test_only_source(source_only_build):
    proc = subprocess.Popen([
        "sage",
        "--source-path",
        source_only_build.src_path,
        "--verbose"],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE)

    (output, error) = proc.communicate()

    assert u"There is no 'compile_commands.json'" in str(output)
