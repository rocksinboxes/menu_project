     ''' tmppath=tempfile.NamedTemporaryFile(dir='/home/pi/', delete=False,suffix='.sh')
        original_path=tmppath.name
        with open(original_path, 'wb') as f:
            f.write(data)
            print(original_path)
            chmod(original_path, 0o755)
            call(original_path)
            f.close()
         '''   
            