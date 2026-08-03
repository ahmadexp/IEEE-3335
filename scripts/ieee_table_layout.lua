-- Give standards tables stable, wrapping column widths in the PDF output.
local widths_by_column_count = {
  [2] = { 0.24, 0.76 },
  [3] = { 0.22, 0.32, 0.46 },
  [4] = { 0.16, 0.19, 0.325, 0.325 },
  [5] = { 0.24, 0.09, 0.12, 0.11, 0.44 },
}

function Table(table_element)
  local widths = widths_by_column_count[#table_element.colspecs]
  if widths == nil then
    return nil
  end

  for index, column_spec in ipairs(table_element.colspecs) do
    table_element.colspecs[index] = { column_spec[1], widths[index] }
  end

  return table_element
end
