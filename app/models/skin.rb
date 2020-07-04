class Skin < ApplicationRecord
  serialize :flags,        Array
  serialize :restrictions, Array
end
