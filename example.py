from grobid_client.grobid_client import GrobidClient as GC
from grobid_client.grobid_client_one_file import GrobidClient as GCOne

if __name__ == "__main__":
    # ファイル群をまとめて解析
    client = GC(config_path="./config.json")

    client.process("processFulltextDocument", "./resources/test_pdf", output="./resources/test_out/",
                   consolidate_citations=True, tei_coordinates=True, force=True)

    # 単一ファイルを指定して解析(ヘッダーのみ)
    client_one = GCOne(config_path="./config.json")
    client_one.process("processHeaderDocument", "../input_files/NLP-QA_Framework_Based_on_LSTM-RNN.pdf",
                       output="../out", tei_coordinates=True, force=True)

# 必須の引数：サービス（'processFulltextDocument'、'processHeaderDocument'、'processReferences'、'processCitationList'のいずれか）
# 任意の引数：
# '-h'または'--help'：この使い方の説明を表示します。
# '--input'：PDFファイルが入っているディレクトリへのパスまたは、参考文献のリストが記載されたテキストファイル（'processCitationList'のみ）へのパス
# '--output'：結果を保存するディレクトリへのパス（任意）
# '--config'：設定ファイルへのパス、デフォルトは'./config.json'
# '--n'：サービスを使用する際の並列処理数
# '--generateIDs'：結果のファイルに対してランダムなxml: idを生成します。
# '--consolidate_header'：GROBIDでヘッダーから抽出されたメタデータを統合します。
# '--consolidate_citations'：GROBIDで抽出された文献参照を統合します。
# '--include_raw_citations'：GROBIDで生の文献参照の抽出を要求します。
# '--include_raw_affiliations'：GROBIDで生の所属の抽出を要求します。
# '--force'：既にtei形式の出力ファイルが存在する場合でも、入力のPDFファイルを再処理します。
# '--teiCoordinates'：抽出された要素に元のPDF座標（バウンディングボックス）を追加します。
# '--segmentSentences'：文章内の文に対して < s > 要素を追加し、文を分割します。
# '--verbose'：処理されたファイルに関する情報をコンソールに表示します。
