from capabilities.capability import capability
import subprocess # used for bash commands (when required), unix-only
from pipes import quote # used to sanitize bash input when complex commands are required, unix-only
import glob

class tasks(capability):

    # various xml tags are grabbed with the grep command:
    def analyze(projectPath):
        if(
        not glob.glob('%s/Linguistics/Lexicon/*' % projectPath) or
        not glob.glob('%s/Linguistics/Reversals/*' % projectPath) or
        not glob.glob('%s/Other/Books/*' % projectPath) or
        not glob.glob('%s/General/*' % projectPath) or
        not glob.glob('%s/Linguistics/Inventory/*' % projectPath) or
        not glob.glob('%s/Anthropology/*' % projectPath) or
        not glob.glob('%s/Linguistics/TextCorpus/*' % projectPath) or
        not glob.glob('%s/Linguistics/Discourse/*' % projectPath)
        ):
            return [None, None, None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None]
        else:
            try:
                # LexEntry
                lexEntryCount = subprocess.check_output( 'grep -r "<LexEntry" \
                %s/Linguistics/Lexicon/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # LexSense
                lexSenseCount = subprocess.check_output( 'grep -r \'class="LexSense"\' \
                %s/Linguistics/Lexicon/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # LexPronunciation
                lexPronunciationCount = subprocess.check_output( 'grep -r \'class="LexPronunciation"\' \
                %s/Linguistics/Lexicon/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # LexExampleSentence
                lexExampleSentenceCount = subprocess.check_output( 'grep -r \'class="LexExampleSentence"\' \
                %s/Linguistics/Lexicon/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # LexReference
                lexReferenceCount = subprocess.check_output( 'grep -r "<LexReference" \
                %s/Linguistics/Lexicon/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # LexEntryRef
                lexEntryRefCount = subprocess.check_output( 'grep -r \'class="LexEntryRef"\' \
                %s/Linguistics/Lexicon/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # ReversalIndex
                reversalIndexCount = subprocess.check_output( 'grep -r "</ReversalIndex>" \
                %s/Linguistics/Reversals/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # ReversalIndexEntry
                reversalIndexEntryCount = subprocess.check_output( 'grep -r "<ReversalIndexEntry" \
                %s/Linguistics/Reversals/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # ScrBook
                scrBookCount = subprocess.check_output( 'grep -r "<ScrBook" \
                %s/Other/Books/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # ScrSection
                scrSectionCount = subprocess.check_output( 'grep -r \'class="ScrSection"\' \
                %s/Other/Books/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # ScrTextPara
                scrTextParaCount = subprocess.check_output( 'grep -r \'class="ScrTextPara"\' \
                %s/Other/Books/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # WfiWordform
                wfiWordformCount = subprocess.check_output( 'grep -r "<WfiWordform" \
                %s/Linguistics/Inventory/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # WfiAnalysis
                wfiAnalysisCount = subprocess.check_output( 'grep -r "<WfiAnalysis" \
                %s/Linguistics/Inventory/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # WfiGloss
                wfiGlossCount = subprocess.check_output( 'grep -r "<WfiGloss" \
                %s/Linguistics/Inventory/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # WfiMorphBundle
                wfiMorphBundleCount = subprocess.check_output( 'grep -r \'class="WfiMorphBundle"\' \
                %s/Linguistics/Inventory/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # Segment
                # segmentCount = subprocess.check_output( 'grep -r "<Segment" \
                # %s/Linguistics/Lexicon/* | wc -l' \
                # % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # Text
                # textCount = subprocess.check_output( 'grep -r "<Text" \
                # %s/Linguistics/Lexicon/* | wc -l' \
                # % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # StTxtPara
                stTxtParaCount = subprocess.check_output( 'grep -r \'class="StTxtPara"\' \
                %s/Linguistics/TextCorpus/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # RnGenericRec
                rnGenericRecCount = subprocess.check_output( 'grep -r "<RnGenericRec" \
                %s/Anthropology/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # CmFile
                cmFileCount = subprocess.check_output( 'grep -r "<CmFile" \
                %s/General/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # CmPicture
                cmPictureCount = subprocess.check_output( 'grep -r \'class="CmPicture"\' \
                %s/Linguistics/Lexicon/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # ConstChartRow
                constChartRowCount = subprocess.check_output( 'grep -r \'class="ConstChartRow"\' \
                %s/Linguistics/Discourse/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # ConstChartTag
                constChartTagCount = subprocess.check_output( 'grep -r \'class="ConstChartTag"\' \
                %s/Linguistics/Discourse/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # DsChart
                dsChartCount = subprocess.check_output( 'grep -r "<DsChart" \
                %s/Linguistics/Discourse/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

                # TextTag
                textTagCount = subprocess.check_output( 'grep -r "<TextTag" \
                %s/Linguistics/TextCorpus/* | wc -l' \
                % quote(projectPath), shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

            except(Exception):
                print('Error!!! a command went wrong...')
            else:
                return [
                int(lexEntryCount),
                int(lexSenseCount),
                int(lexPronunciationCount),
                int(lexExampleSentenceCount),
                int(lexReferenceCount),
                int(lexEntryRefCount),
                int(reversalIndexCount),
                int(reversalIndexEntryCount),
                int(scrBookCount),
                int(scrSectionCount),
                int(scrTextParaCount),
                int(wfiWordformCount),
                int(wfiAnalysisCount),
                int(wfiGlossCount),
                int(wfiMorphBundleCount),
                # int(segmentCount),
                int(stTxtParaCount),
                int(rnGenericRecCount),
                int(cmFileCount),
                int(cmPictureCount),
                int(constChartRowCount),
                int(constChartTagCount),
                int(dsChartCount),
                int(textTagCount)
                ]
            #

        # end of analyze()

    def updateDb(dbConn, py_name, value):
        cur = dbConn.cursor() # cursor to make changes
        cur.execute( """UPDATE project.metadata SET
        classCount_lexEntry = %s,
        classCount_lexSense = %s,
        classCount_lexPronunciation = %s,
        classCount_lexExampleSentence = %s,
        classCount_lexReference = %s,
        classCount_lexEntryRef = %s,
        classCount_reversalIndex = %s,
        classCount_reversalIndexEntry = %s,
        classCount_scrBook = %s,
        classCount_scrSection = %s,
        classCount_scrTextPara = %s,
        classCount_wfiWordform = %s,
        classCount_wfiAnalysis = %s,
        classCount_wfiGloss = %s,
        classCount_wfiMorphBundle = %s,
        classCount_stTxtPara = %s,
        classCount_rnGenericRec = %s,
        classCount_cmFile = %s,
        classCount_cmPicture = %s,
        classCount_constChartRow = %s,
        classCount_constChartTag = %s,
        classCount_dsChart = %s,
        classCount_textTag = %s
        WHERE name = %s;""",
        (value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9],
        value[10], value[11], value[12], value[13], value[14], value[15], value[16], value[17], value[18],
        value[19], value[20], value[21], value[22], py_name) )
        dbConn.commit() # save changes to db

    def getColumns(): # this is synonymous with the lists in updateDb() and analyze()'s return!
        return [
        ['classCount_lexEntry', 'int'],
        ['classCount_lexSense', 'int'],
        ['classCount_lexPronunciation', 'int'],
        ['classCount_lexExampleSentence', 'int'],
        ['classCount_lexReference', 'int'],
        ['classCount_lexEntryRef', 'int'],
        ['classCount_reversalIndex', 'int'],
        ['classCount_reversalIndexEntry', 'int'],
        ['classCount_scrBook', 'int'],
        ['classCount_scrSection', 'int'],
        ['classCount_scrTextPara', 'int'],
        ['classCount_wfiWordform', 'int'],
        ['classCount_wfiAnalysis', 'int'],
        ['classCount_wfiGloss', 'int'],
        ['classCount_wfiMorphBundle', 'int'],
        # ['classCount_segment', 'int'],
        ['classCount_stTxtPara', 'int'],
        ['classCount_rnGenericRec', 'int'],
        ['classCount_cmFile', 'int'],
        ['classCount_cmPicture', 'int'],
        ['classCount_constChartRow', 'int'],
        ['classCount_constChartTag', 'int'],
        ['classCount_dsChart', 'int'],
        ['classCount_textTag', 'int']
        ]
