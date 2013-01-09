import zipfile
import sys
import os
import glob
import re

def decompress_saz(saz_file_name, output_folder="output"):
    try:
        print "[Info] Decompressing saz to folder '%s'" % (output_folder)
        zip_file = zipfile.ZipFile(saz_file_name)
        zip_file.extractall(path=output_folder)
    except Exception, e:
        print "[Exception] " + e.message

def process_request(request_file_name):
    f = open(request_file_name, "r")
    s = f.read()

    #TODO - Add error checking
    re_service = re.compile("POST.*/([^/]+) HTTP*")
    re_service_results = re_service.findall(s)

    re_action = re.compile("SOAPAction.*/([^/]+)\"")
    re_action_results = re_action.findall(s)

    re_post_body = re.compile("\r\n\r\n([^\r\n]*)")
    re_post_body_results = re_post_body.findall(s)

    if not(re_service_results is None or re_action_results is None or re_post_body_results is None):
        return (re_service_results.pop(), re_action_results.pop(), re_post_body_results.pop())
    else:
        return None

def save_processed_request(processed_request, output_folder, processed_folder="processed"):
    (service_name, action_name, soap_request) = processed_request



def iterate_through_session_files(output_folder="output", output_sub_folder="raw"):
    try:
        list_files = glob.glob(output_folder + "/" + output_sub_folder + "/" + "*_c.txt")
        list_files.sort()

        for each_file in list_files:
            processed_request = process_request(each_file)

            if processed_request is not None:
                save_processed_request(processed_request, output_folder)

    except Exception, e:
        pass


if __name__ == '__main__':
    """
    if len(sys.argv) < 2:
        print "usage: python fidses.py <saz-file>"
        sys.exit(-1)

    decompress_saz(sys.argv[1])
    iterate_through_session_files()
    """
    result_tuple = process_request("output/raw/042_c.txt")



