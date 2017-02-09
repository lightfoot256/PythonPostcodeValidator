
# cProfile of Optimised (no print) import without using regular expression

The following lines have been extracted to highlight the slowdown by using string comparison instead of a compiled regular expression:
>
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      8269396    0.941    0.000    0.941    0.000 postcode_validator_without_regex.py:10(match_number)
      2147854    0.452    0.000    0.452    0.000 postcode_validator_without_regex.py:14(match_AtoPRtoUWYZ)
      1845216    0.372    0.000    0.372    0.000 postcode_validator_without_regex.py:18(match_AtoHKtoY)
        95305    0.030    0.000    0.030    0.000 postcode_validator_without_regex.py:22(match_AtoHJKPSTUW)
      4256978    1.158    0.000    1.158    0.000 postcode_validator_without_regex.py:26(match_ABDtoHJLNPtoUWtoZ)
       952174    0.365    0.000    0.365    0.000 postcode_validator_without_regex.py:36(match_ABEHMNPRVWXY)
      2133157    1.810    0.000    3.347    0.000 postcode_validator_without_regex.py:51(match_suffix)
       893040    0.413    0.000    0.413    0.000 postcode_validator_without_regex.py:57(match_double_district)
       924584    0.150    0.000    0.150    0.000 postcode_validator_without_regex.py:75(match_single_district)
      2147854    3.499    0.000    9.315    0.000 postcode_validator_without_regex.py:81(match)

Compared to the compiled regex:
>
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      2147854    0.360    0.000    1.473    0.000 postcode_validator.py:36(match)

The full listing is shown below:
>
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:102(release)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:142(__init__)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:146(__enter__)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:153(__exit__)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:159(_get_module_lock)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:173(cb)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:197(_call_with_frames_removed)
           22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:208(_verbose_message)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:293(__init__)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:297(__enter__)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:304(__exit__)
            8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(<genexpr>)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:355(__init__)
            4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:389(cached)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:402(parent)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:410(has_location)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:493(_init_module_attrs)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:553(module_from_spec)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:57(__init__)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:641(_load_unlocked)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:698(find_spec)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:77(acquire)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:771(find_spec)
            8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:834(__enter__)
            8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:838(__exit__)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:861(_find_spec)
            2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:931(_find_and_load_unlocked)
            2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:958(_find_and_load)
            1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:989(_handle_fromlist)
            5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1080(_path_importer_cache)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1117(_get_spec)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1149(find_spec)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1228(_get_spec)
            4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1233(find_spec)
            4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:263(cache_from_source)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:361(_get_cached)
            4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:37(_relax_case)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:393(_check_name_wrapper)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:430(_validate_bytecode_header)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:485(_compile_bytecode)
            4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:52(_r_long)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:524(spec_from_file_location)
           20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:57(_path_join)
           20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:59(<listcomp>)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:604(_open_registry)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:611(_search_registry)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:626(find_spec)
            4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:63(_path_split)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:669(create_module)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:672(exec_module)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:743(get_code)
            8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:75(_path_stat)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:800(__init__)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:825(get_filename)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:830(get_data)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:840(path_stats)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:85(_path_is_mode_type)
            2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:94(_path_isfile)
            1    0.045    0.045   18.646   18.646 <string>:1(<module>)
            1    0.000    0.000    0.000    0.000 __init__.py:43(normalize_encoding)
            1    0.000    0.000    0.000    0.000 __init__.py:71(search_function)
            3    0.000    0.000    0.000    0.000 _bootlocale.py:11(getpreferredencoding)
            1    0.000    0.000    0.000    0.000 _bootlocale.py:5(<module>)
         4165    0.002    0.000    0.002    0.000 _compression.py:12(_check_not_closed)
            1    0.000    0.000    0.000    0.000 _compression.py:150(tell)
            1    0.000    0.000    0.000    0.000 _compression.py:36(readable)
            1    0.000    0.000    0.000    0.000 _compression.py:39(__init__)
            1    0.000    0.000    0.000    0.000 _compression.py:59(close)
         4164    0.018    0.000    0.339    0.000 _compression.py:66(readinto)
            2    0.000    0.000    0.000    0.000 codecs.py:185(__init__)
            1    0.000    0.000    0.000    0.000 codecs.py:259(__init__)
            1    0.000    0.000    0.000    0.000 codecs.py:93(__new__)
            1    0.000    0.000    0.000    0.000 cp1252.py:17(IncrementalEncoder)
      2147856    0.505    0.000    1.175    0.000 cp1252.py:18(encode)
            1    0.000    0.000    0.000    0.000 cp1252.py:21(IncrementalDecoder)
         4164    0.004    0.000    0.069    0.000 cp1252.py:22(decode)
            1    0.000    0.000    0.000    0.000 cp1252.py:25(StreamWriter)
            1    0.000    0.000    0.000    0.000 cp1252.py:28(StreamReader)
            1    0.000    0.000    0.000    0.000 cp1252.py:3(<module>)
            1    0.000    0.000    0.000    0.000 cp1252.py:33(getregentry)
            1    0.000    0.000    0.000    0.000 cp1252.py:9(Codec)
            1    0.000    0.000    0.000    0.000 gzip.py:123(__init__)
            1    0.000    0.000    0.001    0.001 gzip.py:20(open)
         4164    0.007    0.000    0.369    0.000 gzip.py:278(read1)
      2152027    0.246    0.000    0.246    0.000 gzip.py:298(closed)
            1    0.000    0.000    0.000    0.000 gzip.py:302(close)
            1    0.000    0.000    0.000    0.000 gzip.py:321(flush)
            1    0.000    0.000    0.000    0.000 gzip.py:328(fileno)
            1    0.000    0.000    0.000    0.000 gzip.py:343(readable)
            1    0.000    0.000    0.000    0.000 gzip.py:346(writable)
            1    0.000    0.000    0.000    0.000 gzip.py:349(seekable)
            1    0.000    0.000    0.000    0.000 gzip.py:378(__init__)
            2    0.000    0.000    0.000    0.000 gzip.py:385(_init_read)
            2    0.000    0.000    0.000    0.000 gzip.py:389(_read_exact)
            2    0.000    0.000    0.000    0.000 gzip.py:405(_read_gzip_header)
         4164    0.021    0.000    0.317    0.000 gzip.py:438(read)
         4163    0.006    0.000    0.038    0.000 gzip.py:489(_add_read_data)
            1    0.000    0.000    0.000    0.000 gzip.py:493(_read_eof)
            1    0.000    0.000    0.000    0.000 gzip.py:74(__init__)
         4184    0.015    0.000    0.054    0.000 gzip.py:80(read)
         4163    0.005    0.000    0.006    0.000 gzip.py:93(prepend)
            1    2.794    2.794   18.601   18.601 postcode_importer_part3_optimised.py:28(do_import)
            2    0.950    0.475    5.808    2.904 postcode_importer_part3_optimised.py:76(write_items)
      8269396    0.941    0.000    0.941    0.000 postcode_validator_without_regex.py:10(match_number)
      2147854    0.452    0.000    0.452    0.000 postcode_validator_without_regex.py:14(match_AtoPRtoUWYZ)
      1845216    0.372    0.000    0.372    0.000 postcode_validator_without_regex.py:18(match_AtoHKtoY)
        95305    0.030    0.000    0.030    0.000 postcode_validator_without_regex.py:22(match_AtoHJKPSTUW)
      4256978    1.158    0.000    1.158    0.000 postcode_validator_without_regex.py:26(match_ABDtoHJLNPtoUWtoZ)
       952174    0.365    0.000    0.365    0.000 postcode_validator_without_regex.py:36(match_ABEHMNPRVWXY)
      2133157    1.810    0.000    3.347    0.000 postcode_validator_without_regex.py:51(match_suffix)
       893040    0.413    0.000    0.413    0.000 postcode_validator_without_regex.py:57(match_double_district)
       924584    0.150    0.000    0.150    0.000 postcode_validator_without_regex.py:75(match_single_district)
      2147854    3.499    0.000    9.315    0.000 postcode_validator_without_regex.py:81(match)
            1    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x1DDD9CA8}
            1    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_build}
         4164    0.065    0.000    0.065    0.000 {built-in method _codecs.charmap_decode}
      2147856    0.670    0.000    0.670    0.000 {built-in method _codecs.charmap_encode}
            1    0.000    0.000    0.000    0.000 {built-in method _csv.reader}
            2    0.000    0.000    0.000    0.000 {built-in method _csv.writer}
            2    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
            8    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
            1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
            2    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
           10    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
            3    0.000    0.000    0.000    0.000 {built-in method _locale._getdefaultlocale}
            2    0.000    0.000    0.000    0.000 {built-in method _struct.unpack}
            4    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
            4    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
            5    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
            1    0.000    0.000    0.000    0.000 {built-in method builtins.__import__}
            2    0.000    0.000    0.000    0.000 {built-in method builtins.any}
          3/1    0.000    0.000   18.646   18.646 {built-in method builtins.exec}
           12    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
            9    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
           10    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
      2158149    0.128    0.000    0.128    0.000 {built-in method builtins.len}
            1    0.000    0.000    0.000    0.000 {built-in method builtins.next}
            1    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
            2    1.130    0.565    1.130    0.565 {built-in method builtins.sorted}
            4    0.000    0.000    0.000    0.000 {built-in method from_bytes}
            3    0.004    0.001    0.004    0.001 {built-in method io.open}
            2    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
            7    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
            1    0.000    0.000    0.000    0.000 {built-in method nt.getcwd}
            8    0.000    0.000    0.000    0.000 {built-in method nt.stat}
            4    0.000    0.000    0.000    0.000 {built-in method winreg.OpenKey}
         4165    0.032    0.000    0.032    0.000 {built-in method zlib.crc32}
            2    0.000    0.000    0.000    0.000 {built-in method zlib.decompressobj}
            1    0.000    0.000    0.000    0.000 {function DecompressReader.close at 0x03B39030}
            6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
         4164    0.003    0.000    0.003    0.000 {method 'cast' of 'memoryview' objects}
            2    0.000    0.000    0.000    0.000 {method 'close' of '_io.BufferedReader' objects}
         4163    0.199    0.000    0.199    0.000 {method 'decompress' of 'zlib.Decompress' objects}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
            2    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
            1    0.000    0.000    0.000    0.000 {method 'fileno' of '_io.BufferedReader' objects}
            2    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
            3    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
            6    0.000    0.000    0.000    0.000 {method 'isalnum' of 'str' objects}
           25    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
            2    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
         4183    0.039    0.000    0.039    0.000 {method 'read' of '_io.BufferedReader' objects}
            2    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
         4164    0.020    0.000    0.360    0.000 {method 'read1' of '_io.BufferedReader' objects}
            2    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
           13    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
            4    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
           44    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
            2    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
      2147856    2.549    0.000    3.724    0.000 {method 'writerow' of '_csv.writer' objects}
