#!/usr/bin/env python3


# Copyright 2012-2013 Jussi Pakkanen

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import xml.etree.ElementTree as ET
import xml.dom.minidom

def gen_vcxproj(ofname):
    buildtype = 'Debug'
    platform = "Win32"
    project_name = 'prog'
    target_name = 'prog'
    subsystem = 'console'
    project_file_version = '10.0.30319.1'
    guid = '{4A8C542D-A4C3-AC4A-A85A-E2A893CCB716}'
    root = ET.Element('Project', {'DefaultTargets' : "Build",
                                  'ToolsVersion' : '4.0',
                                  'xmlns' : 'http://schemas.microsoft.com/developer/msbuild/2003'})
    confitems = ET.SubElement(root, 'ItemGroup', {'Label' : 'ProjectConfigurations'})
    prjconf = ET.SubElement(confitems, 'ProjectConfiguration', {'Include' : 'Debug|Win32'})
    p = ET.SubElement(prjconf, 'Configuration')
    p.text= buildtype
    pl = ET.SubElement(prjconf, 'Platform')
    pl.text = platform
    globalgroup = ET.SubElement(root, 'PropertyGroup', Label='Globals')
    guidelem = ET.SubElement(globalgroup, 'ProjectGUID')
    guidelem.text = guid
    kw = ET.SubElement(globalgroup, 'Keyword')
    kw.text = 'Win32Proj'
    ns = ET.SubElement(globalgroup, 'RootNamespace')
    ns.text = 'Sample'
    p = ET.SubElement(globalgroup, 'Platform')
    p.text= platform
    pname= ET.SubElement(globalgroup, 'ProjectName')
    pname.text = project_name
    ET.SubElement(root, 'Import', Project='$(VCTargetsPath)\Microsoft.Cpp.Default.props')
    type_config = ET.SubElement(root, 'PropertyGroup', Label='Configuration')
    ET.SubElement(type_config, 'ConfigurationType').text = 'Application'
    ET.SubElement(type_config, 'CharacterSet').text = 'MultiByte'
    ET.SubElement(type_config, 'WholeProgramOptimization').text = 'false'
    ET.SubElement(type_config, 'UseDebugLibraries').text = 'false'
    ET.SubElement(root, 'Import', Project='$(VCTargetsPath)\Microsoft.Cpp.props')
    direlem = ET.SubElement(root, 'PropertyGroup')
    fver = ET.SubElement(direlem, '_ProjectFileVersion')
    fver.text = project_file_version
    outdir = ET.SubElement(direlem, 'OutDir')
    outdir.text = '.\\'
    intdir = ET.SubElement(direlem, 'IntDir')
    intdir.text = 'obj\\'
    tname = ET.SubElement(direlem, 'TargetName')
    tname.text = target_name
    inclinc = ET.SubElement(direlem, 'LinkIncremental')
    inclinc.text = 'true'

    compiles = ET.SubElement(root, 'ItemDefinitionGroup')
    clconf = ET.SubElement(compiles, 'ClCompile')
    opt = ET.SubElement(clconf, 'Optimization')
    opt.text = 'disabled'
    preproc = ET.SubElement(clconf, 'PreprocessorDefinitions')
    rebuild = ET.SubElement(clconf, 'MinimalRebuild')
    rebuild.text = 'true'
    rtlib = ET.SubElement(clconf, 'RuntimeLibrary')
    rtlib.text = 'MultiThreadedDebugDLL'
    funclink = ET.SubElement(clconf, 'FunctionLevelLinking')
    funclink.text = 'true'
    pch = ET.SubElement(clconf, 'PrecompiledHeader')
    warnings = ET.SubElement(clconf, 'WarningLevel')
    warnings.text = 'Level3'
    debinfo = ET.SubElement(clconf, 'DebugInformationFormat')
    debinfo.text = 'EditAndContinue'
    resourcecompile = ET.SubElement(compiles, 'ResourceCompile')
    respreproc = ET.SubElement(resourcecompile, 'PreprocessorDefinitions')
    link = ET.SubElement(compiles, 'Link')
    ofile = ET.SubElement(link, 'OutputFile')
    ofile.text = '$(OutDir)prog.exe'
    addlibdir = ET.SubElement(link, 'AdditionalLibraryDirectories')
    addlibdir.text = '%(AdditionalLibraryDirectories)'
    subsys = ET.SubElement(link, 'SubSystem')
    subsys.text = subsystem
    gendeb = ET.SubElement(link, 'GenerateDebugInformation')
    gendeb.text = 'true'
    pdb = ET.SubElement(link, 'ProgramDataBaseFileName')
    pdb.text = '$(OutDir}prog.pdb'
    entrypoint = ET.SubElement(link, 'EntryPointSymbol')
    entrypoint.text = 'mainCRTStartup'
    targetmachine = ET.SubElement(link, 'TargetMachine')
    targetmachine.text = 'MachineX86'

    inc_files = ET.SubElement(root, 'ItemGroup')
    ET.SubElement(inc_files, 'CLInclude', Include='prog.h')
    inc_src = ET.SubElement(root, 'ItemGroup')
    ET.SubElement(inc_src, 'ClCompile', Include='prog.cpp')
    ET.SubElement(root, 'Import', Project='$(VCTargetsPath)\Microsoft.Cpp.targets')
    tree = ET.ElementTree(root)
    tree.write(ofname, encoding='utf-8', xml_declaration=True)
    # ElementTree can not do prettyprinting so do it manually
    doc = xml.dom.minidom.parse(ofname)
    open(ofname, 'w').write(doc.toprettyxml())

def gen_solution(ofname):
    solution_guid = '{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}'
    proj_guid = '{4A8C542D-A4C3-AC4A-A85A-E2A893CCB716}'
    target_name = 'Sample'
    target_vcxproj = 'sample.vcxproj'
    ofile = open(ofname, 'w')
    ofile.write('Microsoft Visual Studio Solution File, Format Version 11.00\n')
    ofile.write('# Visual Studio 2010\n')
    prj_line = 'Project("%s") = "%s", "%s", "%s"\n' % (solution_guid, target_name,
                                                       target_vcxproj, proj_guid)
    ofile.write(prj_line)
    ofile.write('EndProject')
    ofile.write('Global')
    indent = '\t' # I shudder
    ofile.write('%sGlobalSection(SolutionConfigurationPlatforms) = preSolution\n' % indent)
    indent = '\t\t'
    ofile.write('%sDebug|Win32 = Debug|Win32\n' % indent)
    indent = '\t'
    ofile.write(indent + 'EndGlobalSection\n')
    ofile.write(indent + 'GlobalSection(ProjectConfigurationPlatforms) = postSolution\n')
    indent = '\t\t'
    ofile.write(indent + proj_guid + '.Debug|Win32.ActiveCfg = Debug|Win32\n')
    ofile.write(indent + proj_guid + '.Debug|Win32.Build.0 = Debug|Win32\n')
    indent = '\t'
    ofile.write(indent + 'EndGlobalSection\n')
    ofile.write(indent + 'GlobalSection(SolutionProperties) = preSolution\n')
    indent = '\t\t'
    ofile.write(indent + 'HideSolutionNode = FALSE\n')
    indent = '\t'
    ofile.write(indent + 'EndGlobalSection')
    ofile.write('EndGlobal\n')

def runtest(base):
    gen_vcxproj(base + '.vcxproj')
    gen_solution(base + '.sln')

if __name__ == '__main__':
    runtest('sample')
