from utils import get_data, get_filtered, data_sorted, output_last_operation
def main():
    data = get_data()
    data = get_filtered(data)
    data = data_sorted(data)
    output_last_operation(data)

if __name__ == '__main__':
    main()



