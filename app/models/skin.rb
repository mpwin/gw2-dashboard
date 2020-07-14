class Skin < ApplicationRecord
  belongs_to :collection, optional: true

  serialize :flags,        Array
  serialize :restrictions, Array
end
